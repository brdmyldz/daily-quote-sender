from pull_quote import pull_quote 
import requests


params = dict()

# FILL BELOW VALUES WITH YOUR CREDENTIALS
params["recipient_instagram_account_id"] = "" 
params["page_id"] = ""
params["page_access_token"] = ""

params["graph_version"] = "v15.0/" #Change this if API versions updates
params["graph_domain"] = "https://graph.facebook.com/"


def send_instagram_message(params):
    endpoint_params = dict()
    endpoint_params["recipient"] = str({"id": params["recipient_instagram_account_id"]})
    endpoint_params["message"] = str({"text": pull_quote()})
    endpoint_params["access_token"] = params["page_access_token"]

    url = params["graph_domain"] + params["graph_version"] + params["page_id"] + "/messages"

    response_data = requests.post(url, data = endpoint_params)
    return response_data


def lambda_handler(event, context):
    response = send_instagram_message(params)

    # ERASE COMMENT OUT FOR DEBUG
    # response = dict()
    # response["url"] = url
    # response["endpoint_params"] = endpointParams
    # response["endpoint_params_pretty"] = json.dumps(endpointParams, indent = 4)
    # response["json_data"] = json.loads(response_data.content)
    # response["json_data_pretty"] = json.dumps(response["json_data"], indent = 4)
    # print("\nURL: " + response["url"])
    # print("\nEndpoint Parameters: " + response["endpoint_params_pretty"])
    # print("\nResponse: " + response["json_data_pretty"])