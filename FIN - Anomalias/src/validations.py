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
    
    rec = app.query(
        KeyConditionExpression=Key('pk').eq(sender)
    )
    
    body = { "send" :  float(send), "salario": float(rec["Items"][0]["salario"])}
    
    if rec['Items'][0]['salario'] <= 2000 and send >= 20000:
        
        return {
            'body': json.dumps(body)
        }