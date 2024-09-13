#!/usr/bin/env python3
"""
web file
"""

import requests
import redis


def get_page(url: str) -> str:
    """ Get page """
    re = redis.Redis()
    key = f"count:{url}"
    res_key = f"result:{url}"

    re.incr(key)
    res = re.get(res_key)
    if res:
        return res.decode('utf-8')
    res = requests.get(url).text
    re.set(key, 0)
    re.setex(res_key, 10, res)
    return res

