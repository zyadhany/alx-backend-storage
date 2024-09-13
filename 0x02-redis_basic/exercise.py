#!/usr/bin/env python3
"""
exercise file
"""

import redis
from functools import wraps
import uuid
from typing import Union, Callable


def count_calls(method: Callable) -> Callable:
    """ Count calls decorator """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Wrapper function """
        if isinstance(self._redis, redis.Redis):
            self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """ Call history decorator """
    @wraps(method)
    def invoker(self, *args, **kwargs):
        """ Wrapper function """
        in_key = f"{method.__qualname__}:inputs"
        out_key = f"{method.__qualname__}:outputs"
        output = method(self, *args, **kwargs)
        if isinstance(self._redis, redis.Redis):
            self._redis.rpush(in_key, str(args))
            self._redis.rpush(out_key, str(output))
        return output
    return invoker


def replay(method: Callable) -> None:
    """ Replay decorator """
    r = redis.Redis()
    name = method.__qualname__
    in_name = f"{name}:inputs"
    out_name = f"{name}:outputs"

    cnt = 0
    if r.exists(name):
        cnt = int(r.get(name))
    print(f"{name} was called {cnt} times:")

    inputs = r.lrange(in_name, 0, -1)
    outputs = r.lrange(out_name, 0, -1)

    for i, o in zip(inputs, outputs):
        i = i.decode('utf-8')
        o = o.decode('utf-8')
        print(f"{name}(*{i}) -> {o}")


class Cache:
    """ Cache class """

    def __init__(self):
        """ Constructor """
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Store data in redis """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None) \
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
