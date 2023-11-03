import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

channel.queue_declare(queue='register')

def is_even(n):
    return n & 1 == 0

def on_request(ch, method, props, body):
    n = int(body)

    print(f" [.] Is even({n})")
    response = is_even(n)

    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id=props.correlation_id),
                     body=str(response))
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='register', on_message_callback=on_request)

print("Awaiting RPC requests")
channel.start_consuming()