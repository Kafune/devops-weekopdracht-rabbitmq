import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='creditcard_queue')
channel.queue_declare(queue='creditcard_validation_queue')

def is_valid_creditcard(creditcardnummer):
    creditcardnummer = creditcardnummer.replace(' ', '').replace('-', '')
    if not creditcardnummer.isdigit():
        return False
    
    reversed_number = creditcardnummer[::-1]
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
    creditcardnummer = body.decode('utf-8')
    is_valid = is_valid_creditcard(creditcardnummer)
    channel.basic_publish(exchange='', routing_key='creditcard_validation_queue', body=str(is_valid))
    print(f"Creditcard: '{creditcardnummer}' valid:'{is_valid}'")

channel.basic_consume(queue='creditcard_queue', on_message_callback=callback, auto_ack=True)
print('Wachten op berichten. Druk op CTRL+C om te stoppen.')
channel.start_consuming()