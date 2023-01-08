from defines import get_credentials, make_api_call

def get_page_access_token(params):
    endpointParams = dict()
    endpointParams["fields"] = "access_token"
    endpointParams["access_token"] = params["access_token"]

    url = params["graph_domain"] + params["page_id"]

    return make_api_call(url, endpointParams, params["debug"])

params = get_credentials()
params["debug"] = "yes"
response = get_page_access_token(params)