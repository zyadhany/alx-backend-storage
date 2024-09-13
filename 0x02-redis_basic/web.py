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
    return requests.get(url).text


if __name__ == "__main__":
    get_page("http://google.com")
