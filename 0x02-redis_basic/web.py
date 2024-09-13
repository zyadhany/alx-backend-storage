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
    def wrapper(url: str) -> str:
        """ Wrapper that:
            - check whether a url's data is cached
            - tracks how many times get_page is called
        """
        client = redis.Redis()
        client.incr(f'count:{url}')
        cached_page = client.get(f'{url}')
        if cached_page:
            return cached_page.decode('utf-8')
        response = fn(url)
        client.set(f'{url}', response, 10)
        return response
    return wrapper


@cache
def get_page(url: str) -> str:
    """ Get page function """
    return requests.get(url).text
