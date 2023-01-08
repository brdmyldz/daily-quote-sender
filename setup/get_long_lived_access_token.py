from defines import get_credentials, make_api_call

def get_long_lived_access_token(params):
    endpointParams = dict()
    endpointParams["grant_type"] = "fb_exchange_token"
    endpointParams["client_id"] = params["client_id"]
    endpointParams["client_secret"] = params["client_secret"]
    endpointParams["fb_exchange_token"] = params["access_token"]

    url = params["endpoint_base"] + "oauth/access_token"

    return make_api_call(url, endpointParams, params["debug"])

params = get_credentials()
params["debug"] = "no"
response = get_long_lived_access_token(params)

print("Long-Lived Access Token: " + response["json_data"]["access_token"])