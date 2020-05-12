import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-2')
table = dynamodb.create_table(
    TableName='finch-cache',
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
            'AttributeName': 'pk',
            'AttributeType': 'S'
        },
	    {
            'AttributeName': 'sk',
            'AttributeType': 'S'
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

print("Table status:", table.table_status)