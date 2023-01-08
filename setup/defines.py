import requests
import json

def get_credentials():
    creds = dict()

    # Sender Information
    creds["access_token"] = "EAAyrE26wd1kBAPqP4IpAZBwmMqGxpPWlMe2DTBuFGAu4ZA8KdRtq0POifZAoZCYNlAv5wECQ1RzLtCNfuqdHDo4raMlsZAZCCzE1L8bhuX3THT0aGv7JeNQZCnDAQ06IpRxsXZBxu5PLPZCBZCZAZClEodZBLnTGWCIzqTG5l4XcxSxY6MAZDZD"
    creds["page_id"] = "119666271001896"
    creds["page_access_token"] = "EAAyrE26wd1kBAPy9Nw3ZChZBXZA0zJZAdBOLKA8ZAZBLdzQrm8r2C3taaCvdZB25td3DsR9sL2LndplJ8P3lZCG4AtH5BnAoiGnalpvH8o1mr5UOBw1xliJZCfjgmZABZAKWxvvkz9Xr7cXyWxnTnq9A5ZARQxDuSDN5FG5QMTVvjeGkkly4rTZAqCjk0"
    creds["instagram_account_id"] = "17841400163593277"
    

    # Recipient Information
    creds["recipient_access_token"] = "EAAyrE26wd1kBAEZAevjlgUD5goFWTx9w9aCiHtY70kJcqt1tDqNrLRl4IgrLZAopoDmy610RFCPEk6m29yhxV769E9fLojDWqKWm9whqYH0ZCkqSHo1GGWmSZBm4T7UMupnQEuCLYdpkHjKm8rDDc7K6LFhj2ZCdBFzdWm5uR9wZDZD"
    creds["recipient_page_id"] = "112752827081578"
    #creds["recipient_instagram_account_id"] = "17841430611951749"
    creds["recipient_instagram_account_id"] = "5210152575751938"

    creds["client_id"] = "3565799670314841"
    creds["client_secret"] = "5aeb3e731773b86599087f4f4ed2f8b5"
    creds["graph_domain"] = "https://graph.facebook.com/"
    creds["graph_version"] = "v15.0"
    creds["endpoint_base"] =  creds["graph_domain"] + creds["graph_version"] + "/"
    creds["debug"] = "no"

    
    return creds

def make_api_call(url, endpointParams, debug = "no"):
    data = requests.get(url, endpointParams)
    
    response = dict()
    response["url"] = url
    response["endpoint_params"] = endpointParams
    response["endpoint_params_pretty"] = json.dumps(endpointParams, indent = 4)
    response["json_data"] = json.loads(data.content)
    response["json_data_pretty"] = json.dumps(response["json_data"], indent = 4)

    if(debug == "yes"):
        display_api_call_data(response)

    return response

def display_api_call_data(response):
    print("\nURL: " + response["url"])
    print("\nEndpoint Parameters: " + response["endpoint_params_pretty"])
    print("\nResponse: " + response["json_data_pretty"])
    