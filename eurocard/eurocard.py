import pika
import time

def is_valid_creditcard(creditcard_number):
    creditcard_number = creditcard_number.replace(' ', '').replace('-', '')
    if not creditcard_number.isdigit():
        return False
    
    reversed_number = creditcard_number[::-1]
    total = 0
    for i, digit in enumerate(reversed_number):
        num = int(digit)
        if i % 2 == 1:
            num *= 2
            if num > 9:
                num -= 9
        total += num
    return total % 10 == 0

def callback(ch, method, properties, body):
    creditcard_number = body.decode('utf-8')
    is_valid = is_valid_creditcard(creditcard_number)
    channel.basic_publish(exchange='creditcard_validation', routing_key='creditcard_validation', body=str(is_valid))
    print(f"Creditcard: '{creditcard_number}' valid:'{is_valid}'")

while True:
    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()
        channel.queue_declare(queue='creditcard_queue')
        channel.exchange_declare(exchange='creditcard_validation', exchange_type='direct')

        channel.basic_consume(queue='creditcard_queue', on_message_callback=callback, auto_ack=True)
        print('Waiting for messages. Press CTRL+C to stop.')
        channel.start_consuming()

    except pika.exceptions.AMQPConnectionError as err:
        print(f"Error: {err}")
        print("Retrying in 5 seconds...")
        time.sleep(5) 
