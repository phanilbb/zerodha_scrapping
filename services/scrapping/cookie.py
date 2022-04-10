from selenium import webdriver
import time
import yaml
import ast
from lib import cache

with open('config.yaml') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)


def get_cookie(context, from_cache=True):
    if from_cache:
        cache = get_cookie_from_cache(context)
        if cache:
            return cache

    print("Fetching cookies by call")

    url = config.get('zerodha', {}).get('end-points', {}).get('base-url')
    user_id = config.get('zerodha', {}).get('credentials', {}).get('user_name')
    password = config.get('zerodha', {}).get('credentials', {}).get('password')
    pin = config.get('zerodha', {}).get('credentials', {}).get('pin')

    # creating object of webdriver and passing driver location path to it
    service = webdriver.firefox.service.Service('/Users/labba.kumar/Desktop/geckodriver')
    service.start()

    # this is optional and for future use.
    options = webdriver.FirefoxOptions()
    # options.add_argument('--headless')  #login page will not pop up when this argument is passed
    options = options.to_capabilities()

    # Creating driver object to load url
    driver = webdriver.Remote(service.service_url, options)
    driver.get(url)
    driver.implicitly_wait(15)

    # loading Username and Password
    driver.find_element_by_id("userid").send_keys(user_id)
    time.sleep(2)
    driver.find_element_by_id("password").send_keys(password)
    time.sleep(1)
    driver.find_element_by_class_name("actions").click()

    # loading Pin number
    driver.find_element_by_id("pin").send_keys(pin)
    time.sleep(1)
    driver.find_element_by_class_name("actions").click()
    time.sleep(1)
    cookies = driver.get_cookies()
    time.sleep(2)
    print(cookies)

    # set cookie to redis
    redis = context.get('redis')
    redis.set("cookies", str(cookies))

    return cookies


def get_cookie_from_cache(context):
    redis = context.get('redis')
    cookies = redis.get("cookies")
    if cookies:
        return ast.literal_eval(cookies.decode('utf-8'))
    return None
