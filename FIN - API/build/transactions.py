import json
import boto3
import decimal 
from boto3.dynamodb.conditions import Key, Attr


def handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    app= dynamodb.Table('finch')
    sender = event['queryStringParameters']['m-sender']
    send = event['queryStringParameters']['m-send']
    receiver = event['queryStringParameters']['m-receiver']


    response = app.query(
        KeyConditionExpression=Key('pk').eq(send)
    )
    print(response)

    if response['Items'][0]['money'] > float(send): 
        body = {
            "response": "No se puede realizar la transaccion"
        } 
    else:
        response2 = app.update_item(
            Key={
                'pk': response['pk'],
                'sk': response['sk']
            },
            UpdateExpression="set finch.money = :r",
            ExpressionAttributeValues={
                ':r': response['Items'][0]['money'] - float(send)


                #':p': "Everything happens all at once.",
                #':a': ["Larry", "Moe", "Curly"]
            },
            ReturnValues="UPDATED_NEW"
        )


    print(response2)