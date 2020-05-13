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
    
    rec = app.query(
        KeyConditionExpression=Key('pk').eq(sender)
    )
    
    responseCont = app.query(
        IndexName='sk-receiver-index',
        KeyConditionExpression=Key('sk').eq(sender) & Key('receiver').eq(receiver)
    )
    
    count = len(responseCont['Items'])+1
    
    #return count
    
    body = { "send" :  float(send), "salario": float(rec["Items"][0]["salario"])}
    body2 = { "send" :  float(send), "money": float(rec['Items'][0]['money'])}
    body3 = { "send" :  float(send), "count": "More than 5"}
    body4 = {"message": "No hubo anomalia"}
    
    if rec['Items'][0]['salario'] <= 2000 and send >= 20000:
        response = app.put_item(
            Item={
                "pk": "transaccion-"+str(rand),
                "sk": sender,
                "m-send": send,
                "receiver": receiver,
                "succesful": True,
                "anomalias ": "Anomalia 1"
            }
        )
        
        return {
            'body': json.dumps(body)
        }
        
    elif send >= 10000 and rec['Items'][0]['money'] <= 100:
        response = app.put_item(
            Item={
                "pk": "transaccion-"+str(rand),
                "sk": sender,
                "m-send": send,
                "receiver": receiver,
                "succesful": True,
                "anomalias ": "Anomalia 2"
            }
        )
        
        return {
            'body': json.dumps(body2)
        }
        
    elif count >= 5: #More than 5 transactions in a single day to the same account.
        response = app.put_item(
            Item={
                "pk": "transaccion-"+str(rand),
                "sk": sender,
                "m-send": send,
                "receiver": receiver,
                "succesful": True,
                "anomalias ": "Anomalia 3"
            }
        )
        
        return {
            'body': json.dumps(body3)
        }
        
    else:
        response = app.put_item(
            Item={
                "pk": "transaccion-"+str(rand),
                "sk": sender,
                "m-send": send,
                "receiver": receiver,
                "succesful": True,
                "anomalias ": "No hay"
            }
        )
        
        return {
            'body': json.dumps(body4)
        }