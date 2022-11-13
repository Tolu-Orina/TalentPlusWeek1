import json
import boto3

# Connect to the dynamodb resource
dynamodb = boto3.resource('dynamodb')

# Isolate the talent_table
talent_table =  dynamodb.Table('talent-tolu-dynamo')

# Get the item
item1 = talent_table.get_item(
    Key = {
        "ID": 1
    }
    )

# Get the Word from the talent table
content = json.dumps(item1['Item']['Word'])
print(content)
    
def lambda_handler(event, context):
    
    
    response = {
        "statusCode": 200,
        "body": content,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
        },
    }
    return response
