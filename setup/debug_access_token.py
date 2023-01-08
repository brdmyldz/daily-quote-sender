from defines import get_credentials, make_api_call
import datetime

def debug_access_token(params):
    endpointParams = dict()
    endpointParams["input_token"] = params["access_token"]
    endpointParams["access_token"] = params["access_token"]

    url = params["graph_domain"] + "/debug_token"

    return make_api_call(url, endpointParams, params["debug"])

params = get_credentials()
params["debug"] = "no"
response = debug_access_token(params)

print("\nData Acess Expires at: ")
print(datetime.datetime.fromtimestamp(response["json_data"]["data"]["data_access_expires_at"]))

print("\nToken Acess Expires at: ")
print(datetime.datetime.fromtimestamp(response["json_data"]["data"]["expires_at"]))