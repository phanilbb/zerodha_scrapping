import redis


class Redis(object):
    def __init__(self):
        self.redis = redis.Redis(
            host='localhost',
            port='6379')

    def set(self, key, val):
        return self.redis.set(key, val)

    def get(self, key):
        val = self.redis.get(key)
        return val
