#!/usr/bin/env python3
"""
web file
"""

import requests
import redis
from functools import wraps


def cache(method):
    """ Cache decorator """
    @wraps(method)
    def invoker(url):
        """ invoker function """
        re = redis.Redis()
        key = f'count:{url}'

        re.incr(key)
        res = re.get(url)
        if res:
            return res.decode('utf-8')
        res = method(url)
        re.set(key, 0)
        re.setex(url, 10, res)
        return res
    return invoker


@cache
def get_page(url: str) -> str:
    return requests.get(url).text
