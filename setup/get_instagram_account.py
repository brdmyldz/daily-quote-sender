from defines import get_credentials, make_api_call

def get_instagram_account(params):
    endpointParams = dict()
    endpointParams["access_token"] = params["access_token"]
    endpointParams["fields"] = "instagram_business_account"

    url = params["endpoint_base"] + params["page_id"]

    return make_api_call(url, endpointParams, params["debug"])

params = get_credentials()
params["debug"] = "no"
response = get_instagram_account(params)

print("\nInstagram Business Account Id: " + response["json_data"]["instagram_business_account"]["id"])