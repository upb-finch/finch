import boto3
import json
import decimal


var AWS = require("aws-sdk");

AWS.config.update({
  region: "us-ohio-2",
  endpoint: "http://localhost:8000"
});

var docClient = new AWS.DynamoDB.DocumentClient();

var table = "finch";
var pk = client;
var sk = "carlos";

var params = {
    TableName:table,
    Item:{
        "pk": client,
        "sk": carlos,
        "money":
        "CI":
        "c-transaccion"
        "m-made":
        "sender":
        "receiver":
        "succeful":
        "anomalias"
        "info":{
            "plot": "Nothing happens at all.",
            "rating": 0
        }
    }
};

console.log("Adding a new item...");
docClient.put(params, function(err, data) {
    if (err) {
        console.error("Unable to add item. Error JSON:", JSON.stringify(err, null, 2));
    } else {
        console.log("Added item:", JSON.stringify(data, null, 2));
    }
});

#actualizar

# Helper class to convert a DynamoDB item to JSON.
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if abs(o) % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)

dynamodb = boto3.resource('dynamodb', region_name='us-ohio-2', endpoint_url="http://localhost:8000")

table = dynamodb.Table('finch')

m-made = 100
m-send = 50

response = table.put_item(
   Item={
        'm-made': m-made,
        'm-send': m-send,
        'info': {
            'plot':"Nothing happens at all.",
            'rating': decimal.Decimal(0)
        }
    }
)

print("PutItem succeeded:")
print(json.dumps(response, indent=4, cls=DecimalEncoder))

#delete
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)

    return {
        "statusCode": 200,
        "body": json.dumps(USER)
    }
