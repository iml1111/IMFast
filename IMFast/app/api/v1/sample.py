import time
from fastapi import HTTPException
from app.response import ok
from . import api


@api.get(
    '/sample/slow',
    summary="Slow API Sample",
    tags=['sample'])
async def slow():
    """It's Slow API Sample api"""
    time.sleep(1)
    return ok()


@api.post(
    '/sample/error',
    summary="Internal Error Sample",
    tags=['sample'])
async def error():
    """Internal Error Sample"""
    return f"Error: {1 / 0}"


@api.put(
    '/sample/bad_request',
    summary="Bad Request Sample",
    tags=['sample'])
async def bad_request_api():
    """It's Bad Request sample api."""
    raise HTTPException(status_code=400, detail='BAD')
