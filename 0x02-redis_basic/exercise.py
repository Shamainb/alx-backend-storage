#!/usr/bin/env python3
import redis
import uuid
from typing import Union, Callable


class Cache:
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        key = str(uuid.uuid4())
        if isinstance(data, (int, float)):
            data = str(data)
        self._redis.set(key, data)
        return key


def get(self, key: str, fn: Callable[[bytes], Union[str, bytes, int, float]] =
        Noe) -> Union[str, bytes, int, float, None]:
    data = self._redis.get(key)
    if data is None:
        return None
    if fn is not None:
        data = fn(data)
        return data

    def get_str(self, key: str) -> str:
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> int:
        return self.get(key, fn=int)
