from datetime import datetime
import time


def get_current_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time


def time_in_range(start, end, x):
    if start <= end:
        return start <= x <= end
    else:
        return start <= x or x <= end


def is_weekend():
    weekday = datetime.today().weekday()
    return weekday == 5 or weekday == 6


def is_within_market_time():
    current_time = time.strptime(get_current_time(), "%H:%M:%S")
    start_time = time.strptime("09:00:00", "%H:%M:%S")
    end_time = time.strptime("15:00:00", "%H:%M:%S")

    return start_time < current_time < end_time and not is_weekend()
