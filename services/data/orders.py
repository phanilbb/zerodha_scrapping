import requests

from helpers import request_helper


def get_orders(cookies, context):
    config = context.get('config')
    base_url = config.get('zerodha', {}).get('end-points', {}).get('base-url')
    orders_url = config.get('zerodha', {}).get('end-points', {}).get('orders')
    url = base_url + "/" + orders_url

    try:
        r = requests.get(url, headers=request_helper.get_headers_from_cookies(cookies))

    except requests.exceptions.ConnectionError as e:
        raise Exception("ConnectionError : " + url)

    if not r:
        raise Exception("Some error occurred : " + str(r))

    response = r.json()
    if "error" in response and response["error"]:
        if "message" in response and response["message"]:
            raise Exception(response["message"])
        if "category" in response and response["category"]:
            raise Exception(response["category"])
        raise Exception("Some error occurred")

    print(response)
    return response
