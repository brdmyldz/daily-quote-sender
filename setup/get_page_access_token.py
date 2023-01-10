from defines import get_credentials, make_api_call

def get_page_access_token(params):
    endpoint_params = dict()
    endpoint_params["fields"] = "access_token"
    endpoint_params["access_token"] = params["access_token"]

    url = params["graph_domain"] + params["page_id"]

    return make_api_call(url, endpoint_params, params["debug"])

params = get_credentials()
params["debug"] = "no"
response = get_page_access_token(params)

print("Page Access Token: " + response["json_data"]["access_token"])