#!/usr/bin/env python3
"""
web file
"""

import requests
import redis


def cache(method):
    """ Cache decorator """
    def wrapper(self, *args):
        """ Wrapper function """
        re = redis.Redis()
        key = f"count:{args[0]}"
        res_key = f"result:{args[0]}"

        re.incr(key)
        res = re.get(res_key)
        if res:
            return res.decode('utf-8')
        res = method(self, args[0])
        re.set(key, 0)
        re.setex(res_key, 10, res)
        return res
    return wrapper


@cache
def get_page(url: str) -> str:
    return requests.get(url).text
