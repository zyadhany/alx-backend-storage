#!/usr/bin/env python3
"""
Main file
"""
import redis

Cache = __import__('exercise').Cache

cache = Cache()


id = cache.store(42)
print(id)
print(cache.get(id))
