import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-2')
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
            'AttributeName': 'pk',
            'AttributeType': 'S'
        },
	    {
            'AttributeName': 'sk',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'receiver',
            'AttributeType': 'S'
        }
    ],
    GlobalSecondaryIndexes=[
        {
            'IndexName': 'sk-receiver-index',
            'KeySchema': [
                {
                    'AttributeName': 'sk',
                    'KeyType': 'HASH'
                },
                { 
                    'AttributeName': 'receiver',
                    'KeyType': 'RANGE'
                }
            ],
            'Projection': {
                'ProjectionType': 'ALL'
            },
            'ProvisionedThroughput': {
                'ReadCapacityUnits': 1,
                'WriteCapacityUnits': 1
            }
        },
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 4,
        'WriteCapacityUnits': 4
    }
)

print("Table status:", table.table_status)