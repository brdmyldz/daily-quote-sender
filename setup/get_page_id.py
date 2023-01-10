from defines import get_credentials, make_api_call

def get_page_id(params):
    endpointParams = dict()
    endpointParams["access_token"] = params["access_token"]

    url = params["endpoint_base"] + "me/accounts"

    return make_api_call(url, endpointParams, params["debug"])

params = get_credentials()
params["debug"] = "no"
response = get_page_id(params)

print("Page Name: " + response["json_data"]["data"][0]["name"])
print("Page ID: " + response["json_data"]["data"][0]["id"])