import boto3

client = boto3.client('apigateway')
lam = boto3.client('lambda')
glue = boto3.client('glue')

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

cachemethod = client.create_resource(
    restApiId = response['id'],
    parentId = response2['items'][0]['id'],
    pathPart = "cache",
)

func = lam.get_function(
    FunctionName='transactions'
)

funccache = lam.get_function(
    FunctionName='cache'
)

arnl = func['Configuration']['FunctionArn']

arnc = funccache['Configuration']['FunctionArn']

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
    type='AWS_PROXY',
    integrationHttpMethod='POST',
    uri='arn:aws:apigateway:us-east-2:lambda:path/2015-03-31/functions/'+arnl+'/invocations'
)


#################################### CACHE METHOD ##############################
response6 = client.put_method(
    restApiId = response['id'],
    resourceId = cachemethod['id'],
    httpMethod='GET',
    authorizationType='NONE'
)

response7 = client.put_integration(
    restApiId = response['id'],
    resourceId = cachemethod['id'],
    httpMethod = 'GET',
    type='AWS_PROXY',
    integrationHttpMethod='POST',
    uri='arn:aws:apigateway:us-east-2:lambda:path/2015-03-31/functions/'+arnc+'/invocations'
)

###################################################################################

deploy = client.create_deployment(
    restApiId = response['id'],
    stageName ='prod'
)

print('https://'+response['id']+'.execute-api.us-east-2.amazonaws.com/prod')

permi = lam.add_permission(
    FunctionName='transactions',
    StatementId='apigateway-finch-aws4',
    Action='lambda:InvokeFunction',
    Principal='apigateway.amazonaws.com',
    SourceArn='arn:aws:execute-api:us-east-2:591336854477:'+response['id']+'/prod/*'
)

permi2 = lam.add_permission(
    FunctionName='cache',
    StatementId='apigateway-finch-aws3',
    Action='lambda:InvokeFunction',
    Principal='apigateway.amazonaws.com',
    SourceArn='arn:aws:execute-api:us-east-2:591336854477:'+response['id']+'/prod/*'
)
