import boto3
from random import randint
 
dynamodb = boto3.resource('dynamodb')
finch_table = dynamodb.Table('finch-cache')
 
finch_data = [
    {
        "pk": "company-01",
        "sk": "client-01",
        "CI": randint(1000000, 9999999),
        "m-made": randint(0, 99999999999999)
    },{
        "pk": "company-01",
        "sk": "client-02",
        "CI": randint(1000000, 9999999),
        "m-made": randint(0, 99999999999999)
    },{
        "pk": "company-01",
        "sk": "client-03",
        "CI": randint(1000000, 9999999),
        "m-made": randint(0, 99999999999999)
    },{
        "pk": "company-01",
        "sk": "client-04",
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