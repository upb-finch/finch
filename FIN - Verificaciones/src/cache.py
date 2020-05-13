import json
import boto3
import random
from random import randint
from boto3.dynamodb.conditions import Key, Attr


def handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    app= dynamodb.Table('finch-cache')
    sender = event['queryStringParameters']['sender']
    
    response = app.query(
        KeyConditionExpression=Key('pk').eq(sender)
    )
    
    info = response["Items"]
    
    if len(response["Items"]) == 0:
        first = ("Camila", "Emmi", "Abigail", "Martin", "Mauricio", "Sara", "Enrique", "Mariana", "Joaquin", "Andres", "Ramiro", "Adrian", "Sergio", "Vivian", "Valeria", "Erica", "Raisa", "Daniela", "Alejandra", "Jazmin", "Liz")
        second = ("Fernandez", "Lopez", "Martinez", "Sanchez", "Perez", "Gomez", "Mercury", "Jackson", "Torrez", "Alvarez", "Ruiz", "Ramirez", "Benitez", "Acosta", "Medina", "Arze", "Rojas", "Molina", "Castro")
        firrst = random.choice(first)
        seccond = random.choice(second)
        name = (firrst + " " + seccond )
        
        company ="company-" + str(randint(1,101))
        CI = randint(1000000, 9999999)
        mmade = randint(0, 99999999999999) 
        
        response = app.put_item(
            Item={
                "pk": sender,
                "sk": company,
                "CI": CI,
                "m-made": mmade,
                "name": name,
            }
        )
        
            
        body = {
            "Client code" : sender,
            "Name": name,
            "Company" : company,
            "CI": CI,
            "Money made": mmade
        }
        
    else:
        body = {
            "Client code" : sender,
            "Name": info[0]["name"],
            "Company" : info[0]["sk"],
            "CI": float(info[0]["CI"]),
            "Money made": float(info[0]["m-made"])
        }
    
    return {
        "statusCode" : 200,
        "body": json.dumps(body)
    }