FROM python:3.8

WORKDIR /rpc_server

COPY rpc_test.py /rpc_server/
COPY requirements.txt /rpc_server/

RUN pip install -r requirements.txt

CMD ["python", "rpc_test.py"]

ENV RABBITMQ_HOST=localhost