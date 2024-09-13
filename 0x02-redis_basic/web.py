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
    def invoker(url) -> str:
        """
        Invoker function
        """
        re = redis.Redis()
        re.incr(f'count:{url}')
        result = re.get(f'result:{url}')
        if result:
            return result.decode('utf-8')
        result = method(url)
        re.set(f'count:{url}', 0)
        re.setex(f'result:{url}', 10, result)
        return result
    return invoker


@cache
def get_page(url: str) -> str:
    """ Get page function """
    return requests.get(url).text
