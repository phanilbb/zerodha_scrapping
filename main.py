# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import yaml

with open('config.yaml') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

from controllers import order

from lib.cache import cache
redis = cache.Redis()


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    context = {
        "config": config,
        "redis": redis
    }
    order.find_executed_orders(context)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
