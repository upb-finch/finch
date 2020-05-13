import boto3
from random import randint
 
dynamodb = boto3.resource('dynamodb')
finch_table = dynamodb.Table('finch-cache')
 
finch_data = [
    {
        "pk": "client-01",
        "sk": "company-01",
        "name": "Enrique",
        "CI": randint(1000000, 9999999),
        "m-made": randint(0, 99999999999999)
    },{
        "pk": "client-02",
        "sk": "company-01",
        "name": "Camila",
        "CI": randint(1000000, 9999999),
        "m-made": randint(0, 99999999999999)
    },{
        "pk": "client-03",
        "sk": "company-01",
        "name": "Emmi",
        "CI": randint(1000000, 9999999),
        "m-made": randint(0, 99999999999999)
    },{
        "pk": "client-04",
        "sk": "company-01",
        "name": "Sara",
        "CI": randint(1000000, 9999999),
        "m-made": randint(0, 99999999999999)
    },
]
 
with finch_table.batch_writer() as batch:
    for data in finch_data:
        batch.put_item(
            Item=data
        )
 
print("Done!")