import boto3

dynamodb = boto3.resource('dynamodb')
teacher_table = dynamodb.Table('transaccion')

transaccion_data = [
    {
        "pk": "client-01",
        "sk": "carlos",
        "money":100,
        "c-transaccion": 1,
   
     },{
        "pk": "company-01",
        "sk": "client-01",
        "CI": 7281,
        "m-made": "1000bs."
    },{
        "pk": "transaccion-01",
        "sender": "client-01",
        "receiver": "client-02",
        "m-made": "50",
        "succesful": "verdadero",
        "anomalias ": ""
    },{
        "pk": "client-02",
        "sk": "Alejandro",
        "money":3000,
        "c-transaccion": 3
    },{
        "pk": "company-01",
        "sk": "client-02",
        "CI": 2564531,
        "m-made": " 3000bs."
    },{
        "pk": "transaccion-02",
        "sender": "client-02",
        "receiver": "client-03",
        "m-made": "100",
        "succesful": "verdadero",
        "anomalias ": "…."
    },{

        "teacher_id": "AA-33",
        "teacher_name": "Sophie Duran",
        "semester": 1,
        "class": "Grammar for newbies"
    },
]

with teacher_table.batch_writer() as batch:
    for teacher in teacher_data:
        batch.put_item(
            Item=teacher
        )

print("Done!")
