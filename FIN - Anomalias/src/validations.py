import boto3
import json
import decimal
import random
from boto3.dynamodb.conditions import Key, Attr
from datetime import datetime

def handler(event, context):
    lambda_client = boto3.client('lambda')
    dynamodb = boto3.resource('dynamodb')
    app= dynamodb.Table('finch')
    send = event['key']
    sender = event['key2']
    receiver = event['key3']
    rand=random.randint(1, 100)
    anomaly = []
    
    rec = app.query(
        KeyConditionExpression=Key('pk').eq(sender)
    )
    
    responseCont = app.query(
        IndexName='sk-receiver-index',
        KeyConditionExpression=Key('sk').eq(sender) & Key('receiver').eq(receiver)
    )
    
    count = len(responseCont['Items'])+1
    
    body = {"message": "La transaccion fue realizada con exito"}
    
    if float(rec['Items'][0]['salario']) <= 2000 and float(send) >= 20000:
        anomaly.append('more than 20000$ for people who earn less than 2000$ a month')

        
    if float(send) >= 10000 and float(rec['Items'][0]['money']) <= 100:
        anomaly.append('higher than 10000$ that leave the sender with less than 100$')

        
    if int(count) >= 5:
        anomaly.append('More than 5 transactions in a single day to the same account')


    response = app.put_item(
        Item={
            "pk": "transaccion-"+str(rand),
            "sk": sender,
            "m-send": send,
            "receiver": receiver,
            "succesful": True,
            "anomalias ": anomaly
        }
    )
        
    return {
        'body': json.dumps(body)
    }