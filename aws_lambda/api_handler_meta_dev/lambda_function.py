import json

def lambda_handler(event, context):
    body = json.loads(event["body"])
    print("Instagram-scoped ID: ")
    print(body["entry"][0]["messaging"][0]["sender"]["id"])
    
    return {
        'statusCode': 200,
        'body': json.dumps("Hello World!")
    }