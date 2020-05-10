import boto3

client = boto3.client('apigateway')
lam = boto3.client('lambda')
im = boto3.client('imagebuilder')

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

response5 = client.put_method(
    restApiId = response['id'],
    resourceId = response3['id'],
    httpMethod='POST',
    authorizationType='AWS_IAM'
)

response4 = client.put_integration(
    restApiId = response['id'],
    resourceId = response3['id'],
    httpMethod = 'POST',
    type='AWS',
    integrationHttpMethod='POST',
    uri='arn:aws:apigateway:us-east-2:lambda:path/2015-03-31/functions/arn:aws:lambda:us-east-2:591336854477:function:transactions/invocations'
)

