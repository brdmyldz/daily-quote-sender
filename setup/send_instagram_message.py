from aws_lambda.daily_quote_sender.pull_quote import pull_quote 
from defines import get_credentials
import requests
import json

def send_instagram_message(params):
    endpointParams = dict()

    endpointParams["recipient"] = str({"id": params["recipient_instagram_account_id"]})
    endpointParams["message"] = str({"text": pull_quote()})
    endpointParams["access_token"] = params["page_access_token"]

    url = params["endpoint_base"] + params["page_id"] + "/messages"

    data = requests.post(url, data = endpointParams)

    response = dict()
    response["url"] = url
    response["endpoint_params"] = endpointParams
    response["endpoint_params_pretty"] = json.dumps(endpointParams, indent = 4)
    response["json_data"] = json.loads(data.content)
    response["json_data_pretty"] = json.dumps(response["json_data"], indent = 4)

    return response

params = get_credentials()
response = send_instagram_message(params)
print("\nURL: " + response["url"])
print("\nEndpoint Parameters: " + response["endpoint_params_pretty"])
print("\nResponse: " + response["json_data_pretty"])