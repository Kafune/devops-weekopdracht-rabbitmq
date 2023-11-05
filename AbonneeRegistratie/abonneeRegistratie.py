from flask import Flask, request
import pika
import uuid
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.INFO, format='%(message)s')

class CreditcardValidatieClient(object):

    def __init__(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='rabbitmq', port=5672, heartbeat=3600))
        self.channel = self.connection.channel()

        result = self.channel.queue_declare(queue='', exclusive=True)
        self.callback_queue = result.method.queue

        self.channel.basic_consume(
            queue=self.callback_queue,
            on_message_callback=self.on_response,
            auto_ack=True)

        self.response = None
        self.corr_id = None

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body.decode('utf-8') == 'True'

    def call(self, n):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(
            exchange='',
            routing_key='register',
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,
                correlation_id=self.corr_id,
            ),
            body=str(n))
        self.connection.process_data_events(time_limit=None)
        return self.response

class NotificatieClient:
    def __init__(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='rabbitmq', port=5672, heartbeat=3600))
        self.channel = self.connection.channel()
        self.channel.exchange_declare(exchange='topic_logs', exchange_type='topic')

    def send_notification(self, routing_key, message):
        self.channel.basic_publish(
            exchange='topic_logs',
            routing_key=routing_key,
            body=message)
        print(f" Sent {routing_key}:{message}" )

    def close_connection(self):
        self.connection.close()

creditcardValidatieClient = CreditcardValidatieClient()
notificatieClient = NotificatieClient()

@app.route('/', methods=['POST'])
def receive_post():
    data = request.get_data()
    decoded_data = data.decode('utf-8')
    logging.info(f"Requesting creditcardValidation({decoded_data})")
    response = creditcardValidatieClient.call(decoded_data)
    logging.info(f"Received: {response}")

    if response:
        notificatieClient.send_notification('publish.subscribe', f'Validated Creditcardnumber: {decoded_data}')

    return "Data received and sent to RabbitMQ successfully!"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080) 

