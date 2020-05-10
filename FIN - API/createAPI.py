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
    httpMethod='GET',
    authorizationType='NONE'
)

response4 = client.put_integration(
    restApiId = response['id'],
    resourceId = response3['id'],
    httpMethod = 'GET',
    type='AWS',
    integrationHttpMethod='POST',
    uri='arn:aws:apigateway:us-east-2:lambda:path/2015-03-31/functions/'+arnl+'/invocations'
)

deploy = client.create_deployment(
    restApiId = response['id'],
    stageName ='prod'
)

print('https://'+response['id']+'.execute-api.us-east-2.amazonaws.com/prod')

permi = lam.add_permission(
    FunctionName=arnl,
    StatementId='apigateway-finch-aws',
    Action='lambda:InvokeFunction',
    Principal='apigateway.amazonaws.com'
)

