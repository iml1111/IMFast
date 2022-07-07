import time
from fastapi import HTTPException
from . import api


@api.get('/sample/slow')
async def slow():
    time.sleep(1)
    return {'msg': 'success'}


@api.get('/sample/error')
async def error():
    return f"Error: {1 / 0}"


@api.get('/sample/bad_request')
async def bad_request_api():
    raise HTTPException(status_code=400, detail='BAD')
