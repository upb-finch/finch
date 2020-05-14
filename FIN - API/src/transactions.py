import boto3
import json
import decimal
from boto3.dynamodb.conditions import Key, Attr

def handler(event, context):
    lambda_client = boto3.client('lambda')
    dynamodb = boto3.resource('dynamodb')
    app= dynamodb.Table('finch')
    app2= dynamodb.Table('finch-cache')
    sender = event['queryStringParameters']['m-sender']
    send = event['queryStringParameters']['m-send']
    receiver = event['queryStringParameters']['m-receiver']
    
    ############## CACHE ##############
    
    cachedata = app2.query(
        KeyConditionExpression=Key('pk').eq(sender)
    )
    
    ###################################

    response = app.query(
        KeyConditionExpression=Key('pk').eq(sender)
    )
    
    rec = app.query(
        KeyConditionExpression=Key('pk').eq(receiver)
    )

    if response['Items'][0]['money'] < float(send): 
        body = {
            "response": "No se puede realizar la transaccion, no cuenta con los fondos suficientes",
            "Client code" : sender,
            "Name": cachedata["Items"][0]["name"],
            "Company" : cachedata["Items"][0]["sk"],
            "CI": float(cachedata["Items"][0]["CI"]),
            "Money made": float(cachedata["Items"][0]["m-made"])
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
        try:
            response3 = app.update_item(
                Key={
                    'pk': rec['Items']['pk'],
                    'sk': rec['Items'][0]['sk']
                },
                UpdateExpression="SET money = :r",
                ExpressionAttributeValues={
                    ':r': rec['Items'][0]['money'] + decimal.Decimal(send)
                },
                ReturnValues="UPDATED_NEW"
            )
        except:
            response2 = app.update_item(
            Key={
                    'pk': response['Items'][0]['pk'],
                    'sk': response['Items'][0]['sk']
                },
                UpdateExpression="SET money = :r",
                ExpressionAttributeValues={
                    ':r': response['Items'][0]['money'] + decimal.Decimal(send)
                },
                ReturnValues="UPDATED_NEW"
            )
            body = {
                "response": "No se puede realizar la transaccion, intente mas tarde",
                "Client code" : sender,
                "Name": cachedata["Items"][0]["name"],
                "Company" : cachedata["Items"][0]["sk"],
                "CI": float(cachedata["Items"][0]["CI"]),
                "Money made": float(cachedata["Items"][0]["m-made"])
            } 
            return {
                "body": json.dumps(body)
            }
        
        
        msg = {"key":send, "key2":sender, "key3": receiver, "at": 50}
        invoke_response = lambda_client.invoke(FunctionName="validations", InvocationType='RequestResponse', Payload=json.dumps(msg))
        print('INVOKE', invoke_response)
        t = invoke_response['Payload']
        j = t.read()
        newj = j.decode('utf-8')
        d = json.dumps(newj)
        print('ANOMALIA', d)
        
        body = {
            "response": "Se pudo realizar la transaccion",
            "Client code" : sender,
            "Name": cachedata["Items"][0]["name"],
            "Company" : cachedata["Items"][0]["sk"],
            "CI": float(cachedata["Items"][0]["CI"]),
            "Money made": float(cachedata["Items"][0]["m-made"]),
            "data": j.decode('utf-8')
        } 
    return {
        "body": json.dumps(body)
    }
