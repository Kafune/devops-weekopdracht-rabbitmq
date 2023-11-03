FROM python:3.8

WORKDIR /AbonneeRegistratie

COPY abonneeRegistratie.py /AbonneeRegistratie/
COPY requirements.txt /AbonneeRegistratie/

RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["python", "abonneeRegistratie.py"]

ENV RABBITMQ_HOST=localhost