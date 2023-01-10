from defines import get_credentials, make_api_call

def get_long_lived_access_token(params):
    endpoint_params = dict()
    endpoint_params["grant_type"] = "fb_exchange_token"
    endpoint_params["client_id"] = params["app_id"]
    endpoint_params["client_secret"] = params["app_secret"]
    endpoint_params["fb_exchange_token"] = params["access_token"]

    url = params["endpoint_base"] + "oauth/access_token"

    return make_api_call(url, endpoint_params, params["debug"])

params = get_credentials()
params["debug"] = "no"
response = get_long_lived_access_token(params)

print("Long-Lived Access Token: " + response["json_data"]["access_token"])