dynamodb = boto3.resource('dynamodb')
table = dynamodb.create_table(
    TableName='finch',
    KeySchema=[
        {
            'AttributeName': 'pk',
            'KeyType': 'HASH'  
        },
        {
            'AttributeName': 'sk',
            'KeyType': 'RANGE'  
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'money',
            'AttributeType': 'N'
        },
        {
            'AttributeName': 'CI',
            'AttributeType': 'N'
        },
        {
            'AttributeName': 'm-made',
            'AttributeType': 'N'
        },
        {
            'AttributeName': 'sender',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'receiver',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'm-send',
            'AttributeType': 'N'
        },
        {
            'AttributeName': 'succesful',
            'AttributeType': 'B'
        },
        {
            'AttributeName': 'Anomalias',
            'AttributeType': 'S'
        },

    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

print("Table status:", table.table_status)