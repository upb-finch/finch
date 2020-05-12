import boto3
from random import randint
 
dynamodb = boto3.resource('dynamodb')
finch_table = dynamodb.Table('finch')
 
finch_data = [
    {
        "pk": "client-01",
        "sk": "Carlos",
        "money":100,
        "c-transaccion": 1,
        "salario": 2000
    },{
        "pk": "company-01",
        "sk": "client-01",
        "CI": randint(1000000, 9999999),
        "m-made": randint(0, 99999999999999)
    },{
        "pk": "transaccion-01",
        "sk": "client-01",
        "m-send": 50,
        "receiver": "client-02",
        "succesful": True,
        "anomalias ": "N/A"
    },{
        "pk": "client-02",
        "sk": "Alejandro",
        "money":3000,
        "c-transaccion": 3,
        "salario": 10000
    },{
        "pk": "company-01",
        "sk": "client-02",
        "CI": randint(1000000, 9999999),
        "m-made": randint(0, 99999999999999)
    },{
        "pk": "transaccion-02",
        "sk": "client-01",
        "receiver": "client-03",
        "m-send": 3000,
        "succesful": False,
        "anomalias ": "Muchas"
    },
]
 
with finch_table.batch_writer() as batch:
    for data in finch_data:
        batch.put_item(
            Item=data
        )
 
print("Done!")