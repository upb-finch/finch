import boto3


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
var m-made = 100;
var m-sender = 50;

// Update the item, unconditionally,

var params = {
    TableName:table,
    Key:{
        "m-made": 100,
        "m-sender": 50 
    },
    UpdateExpression: "set info.rating = :r, info.plot=:p, info.actors=:a",
    ExpressionAttributeValues:{
        ":r":5.5,
        ":p":"Everything happens all at once.",
        ":a":["Larry", "Moe", "Curly"]
    },
    ReturnValues:"UPDATED_NEW"
};

console.log("Updating the item...");
docClient.update(params, function(err, data) {
    if (err) {
        console.error("Unable to update item. Error JSON:", JSON.stringify(err, null, 2));
    } else {
        console.log("UpdateItem succeeded:", JSON.stringify(data, null, 2));
    }
});


























    return {
        "statusCode": 200,
        "body": json.dumps(USER)
    }
