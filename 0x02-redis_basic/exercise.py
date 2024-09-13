#!/usr/bin/env python3
"""
exercise file
"""

import redis
import uuid
from typing import Union


class Cache:
    """ Cache class """

    def __init__(self):
        """ Constructor """
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Store data in redis """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: callable = None) \
            -> Union[str, bytes, int, float]:
        """ Get data from redis """
        data = self._redis.get(key)
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """ Get data from redis """
        return self.get(key, str)

    def get_int(self, key: str) -> int:
        """ Get data from redis """
        return self.get(key, int)
