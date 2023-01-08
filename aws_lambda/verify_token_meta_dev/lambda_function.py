import json

def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps(int(event["multiValueQueryStringParameters"]["hub.challenge"][0]))
    }