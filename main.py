from flask import Flask,request

import json
from json import dumps
from kafka import KafkaProducer

topic_name='captured_data'

producer = KafkaProducer(
    bootstrap_servers='{}',
    sasl_mechanism='SCRAM-SHA-256',
    security_protocol='SASL_SSL',
    sasl_plain_username='{}',
    sasl_plain_password='{}',
    value_serializer=lambda x: dumps(x).encode('utf-8')
)

app=Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World"

@app.route('/publish_data',methods=['POST'])
def messagepasser():
    try:
        message=request.json
        print("Input Message : ",message)
        print("Sending kafka message")
        resp = producer.send(topic_name, value=message)
        print(resp)
        print("Sent message to kafka")
        return "Success"
    except:
        return "Error"

if __name__=='__main__':
    app.run(host='0.0.0.0',port=50000)
