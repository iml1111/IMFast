"""App Decorator"""
from functools import wraps


def hello_deco(func):
    """decorator Example"""
    @wraps(func)
    async def wrapper(*args, **kwargs):
        result = await func(*args, **kwargs)
        return result
    return wrapper
