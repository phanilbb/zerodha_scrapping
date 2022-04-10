

def get_headers_from_cookies(cookies):
    cookie = {}
    for each_cookie in cookies:
        cookie[each_cookie.get('name')] = each_cookie.get('value')
        if each_cookie.get('name') == "enctoken":
            enctoken = each_cookie.get('value')

    headers = {
        "Cookie": str(cookie),
        "Authorization": "enctoken " + enctoken
    }

    return headers