FROM python:3.8

WORKDIR /eurocard

COPY eurocardtest.py /eurocard/
COPY requirements.txt /eurocard/

RUN pip install -r requirements.txt

CMD ["python", "eurocardtest.py"]

ENV RABBITMQ_HOST=localhost