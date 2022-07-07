"""Response Shortcuts"""
from fastapi.responses import ORJSONResponse as orjson_res


def ok(result=None):
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


def created(result=None):
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


def bad_request(description):
    return orjson_res(
        {'msg': 'bad_request', 'description': description},
        status_code=400
    )


bad_access_token = orjson_res(
    {
        'msg':'unauthorized',
        'description': "bad_access_token"
    },
    status_code=401,
)


def forbidden(description):
    return orjson_res(
        {
            'msg': 'forbidden',
            'description': description
        }, status_code=403,
    )


not_found = orjson_res(
    {
        'msg': 'not_found',
        'description': "resource not found"
    },
    status_code=404
)
