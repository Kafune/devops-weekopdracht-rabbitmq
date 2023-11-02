# Opdracht

## Voorbereiding
* Zorg dat je Docker geinstalleerd en werkend hebt
* Lees uit het boek van Sander Hoogendoorn (Pragmatisch Modelleren met UML) de [pagina's 2, 3 en 4](https://books.google.nl/books?id=6xZS5GL0d1MC&pg=PA1&hl=nl&source=gbs_toc_r&cad=3) over Dare2Date.

## Casus Dare2Date

### Inleiding
Er zijn verschillende processen binnen de datingservice die niet synchroon geïmplementeerd kunnen worden met bijvoorbeeld een webservice. In deze opdracht ga je gebruik maken van RabbitMQ en op twee manieren een service realiseren:

* Point to point:       Queues
* Publish-Subscribe:    Topics

### UML Diagrammen
Gegeven is het onderstaande use case model en een sequencediagram. De KandidaatAbonnee is een menselijke actor die vanuit een browser of app een HTTP POST doet met een AbonneeAanvraag, de EuroCard, Uitgever en Abonnee zijn externe systemen die luisteren naar binnenkomende berichten. EuroCard is via een queue gekoppeld aan de webservice en geeft true terug als het credicardnummer even is en false als het oneven is. De Uitgever en Abonnee luisteren naar een topic en het enige dat zij doen is de binnenkomende notificatie printen/loggen.

![Use Case Model Dare2Date](https://gitlab.devops.aimsites.nl/rabbitmq/workshop-rabbitmq/-/raw/main/opdracht/Dare2Date/Use%20Case%20Model/Dare2Date.png "Use Case Model Dare2Date")

![Happy Flow Dare2Date](http://gitlab.devops.aimsites.nl/rabbitmq/workshop-rabbitmq/-/raw/main/opdracht/Dare2Date/Happy%20Flow/Happy%20Flow.png "Happy Flow  Dare2Date")

Er zijn uiteindelijke 5 deelsystemen die in een eigen Docker container draaien, getuige het deployment diagram:

![Deployment Dare2Date](http://gitlab.devops.aimsites.nl/rabbitmq/workshop-rabbitmq/-/raw/main/opdracht/Dare2Date/Deployment/Deployment%20Dare2Date.png "Deployment Dare2Date")

* De AbonneeRegistratie webservice die samenwerkt (lokale functieaanroepen in-process) met de classes CreditcardValidatieClient en NotificatieClient
* De EuroCard service 
* De Uitgever service
* De Abonnee service
* De RabbitMQ Broker

### Opdrachtdetaillering

Realiseer in een team de weergegeven deelsystemen met _minimaal twee_ verschillende programmeertalen (er zijn [legio clients/frameworks](https://www.rabbitmq.com/devtools.html)) waarbij je minimaal 1 *queue* en een 1 *topic* gebruikt. Deploy elk deelsysteem in een eigen Docker container. Elk teamlid maakt typisch 1 service (bij 4 teamleden). Lever de opdracht in in een gezamenlijke (privé) git repository waarbij je met 1 enkele docker-compose instructie alle deelsystemen en de RabbitMQ broker kan starten. Schrijf een README.md ([MS standaard](https://docs.microsoft.com/en-us/azure/devops/repos/git/create-a-readme?view=azure-devops)) waarmee de beoordelaar het direct kan uitvoeren op zijn/haar eigen systeem. Maak een issue aan voor de beoordeling en assign deze aan de docent (toegang geven tot prive repo).

### Beoordelingsmodel (2021)

- A. Voldoet aan functionele eisen
   - 10 Volledig (4 van de 4)
   - 7 Grotendeels (3 van de 4)
   - 5 Beperkt (2 van de 4)
   - 1 Nauwelijks (1 van de 4)
- B. Aantal verschillende programmeertalen
   - 10 meer dan 2
   - 7 Precies 2
   - 5 Precies 1
   - 1 Geen (0)
- C. Codekwaliteit (clean code, tests, etc.) 
   - 10 Clean code en voorzien van unittests
   - 7 Clean code
   - 5 Code bevat maximaal vijf verschillende bad smells
   - 1 Code bevat meer dan vijf verschillende bad smells
- D. Deploybaar op Docker
   - 10 Volledig (4 van de 4 services)
   - 7 Grotendeels (3 van de 4)
   - 5 Beperkt (2 van de 4)
   - 1 Nauwelijks (1 van de 4) 
- E. README
   - 10 100% uitvoerbaar
   - 7 Met 1 of 2 omissies uitvoerbaar
   - 5 Onvoldoende overdraagbaar
   - 1 Ontbreekt of is leeg
- F. Teamwork (Knockout)
  - JA 
  - NEE

Als tabel: 

| | 10                             | 7                                    | 5                               | 1                                                 | Weging                                            |
|------------------------------------|--------------------------------------|---------------------------------|---------------------------------------------------|---------------------------------------------------|-----|
| **Voldoet aan functionele eisen**  | Volledig (4 van de 4 services)       | Grotendeels (3 van de 4)        | Beperkt (2 van de 4)                              | Nauwelijks (1 van de 4)                           | 40% |
| **Aantal verschillende programmeertalen** | meer dan 2                           | 2                               | 1                                                 | 0                                                 | 20% |
| **Codekwaliteit** (clean code, tests etc.) | Clean code en voorzien van unittests | Clean code                      | Code bevat maximaal vijf verschillende bad smells | Code bevat meer dan vijf verschillende bad smells | 10% |
| **Deploybaar op Docker**            | Volledig (4 van de 4 services)       | Grotendeels (3 van de 4)        | Beperkt (2 van de 4)                              | Nauwelijks (1 van de 4)                           | 20% |
| **README**                          | 100% uitvoerbaar                     | Met 1 of 2 omissies uitvoerbaar | Onvoldoende overdraagbaar                         | Ontbreekt of is leeg                              | 10% |
| **Teamwork** (Knockout)             |                                      |                                 |                                                   |                                                   | JA/NEE  |

