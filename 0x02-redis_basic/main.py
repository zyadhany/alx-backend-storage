#!/usr/bin/env python3
"""
Main file
"""
import redis
from exercise import replay

Cache = __import__('exercise').Cache

cache = Cache()


for i in range(5):
    cache.store(i)

replay(cache.store)