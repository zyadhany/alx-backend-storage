#!/usr/bin/env python3
"""
web file
"""

import requests
import redis
from functools import wraps


def get_page(url: str) -> str:
    """ Get page function """
    re = redis.Redis()
    re.incr(f"count:{url}")
    res = re.get(url)
    if res:
        return res.decode('utf-8')
    res = requests.get(url).text
    re.setex(url, 10, res)
    return res
