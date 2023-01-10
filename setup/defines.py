import requests
import json

def get_credentials():
    creds = dict()

    # FILL BELOW VALUES WITH YOUR CREDENTIALS
    creds["access_token"] = ""
    creds["app_id"] = ""
    creds["app_secret"] = ""
    creds["page_id"] = ""
    creds["page_access_token"] = ""
    creds["recipient_instagram_account_id"] = ""
    creds["graph_version"] = "v15.0" #Change this if API versions updates

    creds["graph_domain"] = "https://graph.facebook.com/"
    creds["endpoint_base"] =  creds["graph_domain"] + creds["graph_version"] + "/"
    creds["debug"] = "no"

    
    return creds

def make_api_call(url, endpoint_params, debug = "no"):
    data = requests.get(url, endpoint_params)
    
    response = dict()
    response["url"] = url
    response["endpoint_params"] = endpoint_params
    response["endpoint_params_pretty"] = json.dumps(endpoint_params, indent = 4)
    response["json_data"] = json.loads(data.content)
    response["json_data_pretty"] = json.dumps(response["json_data"], indent = 4)

    if(debug == "yes"):
        display_api_call_data(response)

    return response

def display_api_call_data(response):
    print("\nURL: " + response["url"])
    print("\nEndpoint Parameters: " + response["endpoint_params_pretty"])
    print("\nResponse: " + response["json_data_pretty"])
    