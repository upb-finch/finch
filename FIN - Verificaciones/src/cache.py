import json
import boto3
from boto3.dynamodb.conditions import Key, Attr


def handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    app= dynamodb.Table('finch-cache')
    sender = event['queryStringParameters']['sender']
    
    response = app.query(
        KeyConditionExpression=Key('pk').eq(sender)
    )
    
    body = {
        "Client code" : sender,
        "Name": response["Items"][0]["name"],
        "Company" : response["Items"][0]["sk"],
        "CI": float(response["Items"][0]["CI"]),
        "Money made": float(response["Items"][0]["m-made"])
    }
    
    return {
        "statusCode" : 200,
        "body": json.dumps(body)
    }