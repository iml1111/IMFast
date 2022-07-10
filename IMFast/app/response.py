"""Response Shortcuts"""
from typing import Any
from uuid import uuid4
from fastapi.encoders import jsonable_encoder
from fastapi.responses import ORJSONResponse as orjson_res
from pydantic import BaseModel


class Response200ModelFactory:

    def __getitem__(self, result_type):
        class ResponseModel200(BaseModel):
            msg: str = 'ok'
            result: result_type
        # Class Anonymization
        class_obj = ResponseModel200
        class_obj.__name__ = (
                result_type.__name__ + str(uuid4()))
        return class_obj

    def __call__(self, result: Any = None):
        result = jsonable_encoder(result)
        return orjson_res(
            {'msg': 'ok', 'result': result},
            status_code=200,
        )

OK = Response200ModelFactory()


class Response201ModelFactory:

    def __getitem__(self, result_type):
        class ResponseModel201(BaseModel):
            msg: str = 'created'
            result: result_type
        # Class Anonymization
        class_obj = ResponseModel201
        class_obj.__name__ = (
                result_type.__name__ + str(uuid4()))
        return class_obj

    def __call__(self, result: Any = None):
        result = jsonable_encoder(result)
        return orjson_res(
            {'msg': 'created', 'result': result},
            status_code=201,
        )

CREATED = Response201ModelFactory()


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
