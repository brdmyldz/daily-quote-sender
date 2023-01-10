from defines import get_credentials, make_api_call
import datetime

def debug_access_token(params):
    endpoint_params = dict()
    endpoint_params["input_token"] = params["access_token"]
    endpoint_params["access_token"] = params["access_token"]

    url = params["graph_domain"] + "/debug_token"

    return make_api_call(url, endpoint_params, params["debug"])

params = get_credentials()
params["debug"] = "no"
response = debug_access_token(params)

print("\nData Acess Expires at: ")
print(datetime.datetime.fromtimestamp(response["json_data"]["data"]["data_access_expires_at"]))

print("\nToken Acess Expires at: ")
print(datetime.datetime.fromtimestamp(response["json_data"]["data"]["expires_at"]))