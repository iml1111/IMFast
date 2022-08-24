"""App Decorator"""
import time
from functools import wraps
from settings import settings


def hello_deco(func):
    """decorator Example"""
    @wraps(func)
    async def wrapper(*args, **kwargs):
        result = await func(*args, **kwargs)
        return result
    return wrapper
