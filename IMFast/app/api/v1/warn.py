import time
from . import api


@api.get('/warn/slow')
async def slow():
    time.sleep(1)
    return {'msg': 'success'}