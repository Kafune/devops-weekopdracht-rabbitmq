# RabbitMQ Weekopdracht 4

Voor deze opdracht hebben Kachung Li, Roy van de Wiel en Wijnand van Zyl een aantal microservices gemaakt die met elkaar communiceren via RabbitMQ. Bij het realiseren van deze microservices zijn de volgende talen gebruikt:

- Javascript -> Abonneeservice
- Python -> Eurocardservice
- Java -> AbonneeRegistratieservice & Publisherservice

TODO: Screenshot of GIF toevoegen van werking RabbitMQ

## Werking

De AbonneeRegistratie service stuurt een bericht via RabbitMQ naar de EuroCard om aan te geven dat de gebruiker kan registreren. Deze checkt of het creditcardnummer dat is opgegeven is legitiem is of niet. Als het creditcardnummer even is, is hij legitiem. Wanneer het credicardnummer oneven is het creditcardnummer vals. De uitkomst hiervan stuurt de publisher terug naar AbonneeRegistratie. Wannneer AbonneerRegistratite terugkrijgt dat het credicarnummer legitiem is, stuurt hij de gegevens via RabbitMQ door naar Subscriber en Publischer. Deze printen de credicardgegevens vervolgens uit. 

## Hoe gebruik ik de applicatie met RabbitMQ?

### Abonneeregistratie

- Gaat in de folder van AbonneeRegistartie zitten.
- ``` docker build -t <naam-image> ``` waarbij ```<naam-image>``` de naam is die je aan de image wil geven. Deze maakt een image van ```abonneeRegistartie.py```.
- ``` docker run -p 8080:8080 <naam-image> ``` waarbij ```<naam-image>``` de naam is die je aan de image hebt gegeven in de vorige command. Deze build de image op <http://172.17.0.4:8080/>. Dit is de localhost op poort 8080.
- stuur credicardnummer door via volgende command: ```curl -X POST -d <creditcardnummer> http://localhost:8080``` waarbij ```<credicardnummer>``` een string is van een creditcardnummer dat alleen bestaaat uit cijfers. Een voorbeeld hiervan kan dus zijn : ```35742527542722```

#### logging

Bij Abonneeregistratie is logging toegevoegd. De volgende logs zeggen het volgende over Abonneeregistratie:

- ```Requesting credicardValidation(<creditcardnummer>)``` stuurt ```<credicardnummer>``` door naar Eurocard.
- ```Received: <boolean>``` heeft ```<Boolean>``` ontvangen van Eurocard.
- ```"Data received and sent to RabbitMQ successfully!"``` als bericht is verstuurd naar subscriber/publisher en verwerkt in RabbitMQ.

#### Routing/keys

routing/keys voor de twee classes

##### CreditcardValidatieClient

- Exchange: ''
- Routing_Key: 'register'

#### NotificatieClient

- Exchange: 'topic_logs'
- routing_key: 'publish.subscribe'

Voor Publish moet routing_key dus 'publish.*' worden.
Voor Subscribe moet routing_key dus '*.subscribe' worden.