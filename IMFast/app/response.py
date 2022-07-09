"""Response Shortcuts"""
from typing import Any
from fastapi.responses import ORJSONResponse as orjson_res


def ok(result: Any = None):
    if result is None:
        return orjson_res(
            {'msg': 'ok'},
            status_code=200
        )
    else:
        return orjson_res(
            {'msg': 'ok', 'result': result},
            status_code=200,
        )


def created(result: Any = None):
    if result is None:
        return orjson_res(
            {'msg': 'created'},
            status_code=201
        )
    else:
        return orjson_res(
            {'msg': 'created', 'result': result},
            status_code=201,
        )


no_content = orjson_res({}, status_code=204)


def bad_request(detail: str):
    return orjson_res(
        {'msg': 'bad_request', 'detail': detail},
        status_code=400,

    )

def bad_jwt_token(detail: str):
    return orjson_res(
        {
            'msg': 'bad_jwt_token',
            'detail': detail
        },
        status_code=401,
        headers={"WWW-Authenticate": "Bearer"},
    )



def forbidden(detail: str):
    return orjson_res(
        {
            'msg': 'forbidden',
            'detail': detail
        }, status_code=403,
    )


not_found = orjson_res(
    {
        'msg': 'not_found',
        'detail': "resource not found"
    },
    status_code=404
)
