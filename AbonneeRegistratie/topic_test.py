import pika

class NotificationReceiver:
    def __init__(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost', heartbeat=3600))
        self.channel = self.connection.channel()
        self.channel.exchange_declare(exchange='topic_logs', exchange_type='topic')

        result = self.channel.queue_declare('', exclusive=True)
        self.queue_name = result.method.queue

    def bind_queue(self, routing_key):
        self.channel.queue_bind(exchange='topic_logs', queue=self.queue_name, routing_key=routing_key)

    def receive_and_print(self, ch, method, properties, body):
        print(f" Received Creditcardnumber: {body}")

    def start_consuming(self):
        self.channel.basic_consume(queue=self.queue_name, on_message_callback=self.receive_and_print, auto_ack=True)
        print(' Waiting for messages. To exit, press Ctrl+C')
        self.channel.start_consuming()

if __name__ == '__main__':
    receiver = NotificationReceiver()
    receiver.bind_queue('*.subscribe')
    receiver.start_consuming()
