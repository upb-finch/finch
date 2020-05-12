import boto3
import json
import decimal
from boto3.dynamodb.conditions import Key, Attr
from datetime import datetime

def handler(event, context):
    lambda_client = boto3.client('lambda')
    dynamodb = boto3.resource('dynamodb')
    app= dynamodb.Table('finch')
    sender = event['queryStringParameters']['m-sender']
    send = event['queryStringParameters']['m-send']
    receiver = event['queryStringParameters']['m-receiver']

    response = app.query(
        KeyConditionExpression=Key('pk').eq(sender)
    )
    
    rec = app.query(
        KeyConditionExpression=Key('pk').eq(receiver)
    )
    
    print(response)

    if response['Items'][0]['money'] < float(send): 
        body = {
            "response": "No se puede realizar la transaccion"
        } 
    else:
        response2 = app.update_item(
            Key={
                'pk': response['Items'][0]['pk'],
                'sk': response['Items'][0]['sk']
            },
            UpdateExpression="SET money = :r",
            ExpressionAttributeValues={
                ':r': response['Items'][0]['money'] - decimal.Decimal(send)
            },
            ReturnValues="UPDATED_NEW"
        )
        
        response3 = app.update_item(
            Key={
                'pk': rec['Items'][0]['pk'],
                'sk': rec['Items'][0]['sk']
            },
            UpdateExpression="SET money = :r",
            ExpressionAttributeValues={
                ':r': rec['Items'][0]['money'] + decimal.Decimal(send)
            },
            ReturnValues="UPDATED_NEW"
        )
        
        msg = {"key":"new_invocation", "at": datetime.now()}
        invoke_response = lambda_client.invoke(FunctionName="validations", InvocationType='Event', Payload=json.dumps(msg))
        print(invoke_response)
