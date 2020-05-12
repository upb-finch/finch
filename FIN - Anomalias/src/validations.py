import boto3
import json
import decimal
from boto3.dynamodb.conditions import Key, Attr
from datetime import datetime

def handler(event, context):
    lambda_client = boto3.client('lambda')
    dynamodb = boto3.resource('dynamodb')
    app= dynamodb.Table('finch')
    send = event['key']
    sender = event['key2']
    receiver = event['key3']
    
    rec = app.query(
        KeyConditionExpression=Key('pk').eq(sender)
    )
    
    body = { "send" :  float(send), "salario": float(rec["Items"][0]["salario"])}
    body2 = {"message": "No hubo anomalia"}
    
    return {
        'body': json.dumps(body2)
    }
    
    if rec['Items'][0]['salario'] <= 2000 and send >= 20000:
        response = app.put_item(
            Item={
                "pk": "transaccion-05",
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