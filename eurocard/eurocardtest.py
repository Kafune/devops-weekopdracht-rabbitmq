import pika

# Maak een verbinding met RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# De naam van de wachtrij waarnaar je het bericht wilt sturen
queue_name = 'creditcard_queue'

# Het bericht dat je wilt verzenden
message = '6703 4444 4444 4449'  # Vervang dit door het gewenste creditcardnummer

# Publiceer het bericht naar de wachtrij
channel.basic_publish(exchange='', routing_key=queue_name, body=message)

print(f" [x] Verzonden '{message}' naar {queue_name}")

# Sluit de verbinding
connection.close()
