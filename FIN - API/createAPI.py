import boto3

client = boto3.client('apigateway')
lam = boto3.client('lambda')

response = client.create_rest_api(
    name='finch-API',
    endpointConfiguration={
        'types': [
            'REGIONAL',
        ]
    },
)

response2 = client.get_resources(
    restApiId=response['id'],
)

response3 = client.create_resource(
    restApiId = response['id'],
    parentId = response2['items'][0]['id'],
    pathPart = "transaction",
)

func = lam.get_function(
    FunctionName='transactions'
)
arnl = func['Configuration']['FunctionArn']

response4 = client.put_integration(
    restApiId = response['id'],
    resourceId = response3['id'],
    httpMethod = 'POST',
    type='AWS',
    integrationHttpMethod='POST'
)

