import time
from . import api


@api.get('/sample/slow')
async def slow():
    time.sleep(1)
    return {'msg': 'success'}
