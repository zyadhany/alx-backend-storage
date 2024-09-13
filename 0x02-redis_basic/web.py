#!/usr/bin/env python3
"""
web file
"""

import requests
import redis


def get_page(url: str) -> str:
    """ Get page """
    r = redis.Redis()
    key = f"count:{url}"
    r.incr(key)
    if r.get(key) and int(r.get(key)) % 10 == 0:
        r.setex(f"cached:{url}", 10, requests.get(url).text)
    if r.get(f"cached:{url}"):
        return r.get(f"cached:{url}").decode('utf-8')
    return requests.get(url).text
