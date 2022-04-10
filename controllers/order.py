import time

from services.scrapping import cookie
from services.data import orders
from helpers import time_helper


def find_executed_orders(context):
    cookies = cookie.get_cookie(context)

    while True:
        time.sleep(60)

        if not time_helper.is_within_market_time():
            print("Market not opened : " + time_helper.get_current_time())
            continue

        print("Fetching executed orders : " + time_helper.get_current_time())
        orders_response = orders.get_orders(cookies, context)

        if orders_response.get('status') == "success" and orders_response.get('data'):
            print(orders_response['data'])
        else:
            cookie.get_cookie(context, False)
            print("some error")



