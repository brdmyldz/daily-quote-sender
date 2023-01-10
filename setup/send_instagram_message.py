from defines import get_credentials
import requests
import json

def send_instagram_message(params):
    endpoint_params = dict()

    endpoint_params["recipient"] = str({"id": params["recipient_instagram_account_id"]})
    endpoint_params["message"] = str({"text": "Hello World!"})
    endpoint_params["access_token"] = params["page_access_token"]

    url = params["endpoint_base"] + params["page_id"] + "/messages"

    response_data = requests.post(url, data = endpoint_params)
    return response_data

params = get_credentials()
response_data = send_instagram_message(params)

# ERASE COMMENT OUT FOR DEBUG
# response = dict()
# response["url"] = url
# response["endpoint_params"] = endpoint_params
# response["endpoint_params_pretty"] = json.dumps(endpoint_params, indent = 4)
# response["json_data"] = json.loads(response_data.content)
# response["json_data_pretty"] = json.dumps(response["json_data"], indent = 4)
# print("\nURL: " + response["url"])
# print("\nEndpoint Parameters: " + response["endpoint_params_pretty"])
# print("\nResponse: " + response["json_data_pretty"])