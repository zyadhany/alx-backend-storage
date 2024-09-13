#!/usr/bin/env python3
"""
exercise file
"""

import redis
import uuid


class Cache:
    """ Cache class """

    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def stor(self, data) -> str:
        """ Store data in redis """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
