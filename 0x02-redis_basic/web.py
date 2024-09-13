#!/usr/bin/env python3
"""
web file
"""

import requests
import redis
from functools import wraps
from typing import Callable


redis_store = redis.Redis()
""" Redis store """


def casher(method: Callable) -> Callable:
    """ Casher decorator """
    @wraps(method)
    def invoker(url) -> str:
        """ wrapped"""
        redis_store.incr(f'count:{url}')
        result = redis_store.get(f'result:{url}')
        if result:
            return result.decode('utf-8')
        result = method(url)
        redis_store.set(f'count:{url}', 0)
        redis_store.setex(f'result:{url}', 10, result)
        return result
    return invoker


@casher
def get_page(url: str) -> str:
    """ Get page function """
    return requests.get(url).text
