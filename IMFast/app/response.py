"""Response Shortcuts"""
from typing import Any, Optional
from uuid import uuid4
from fastapi import Response, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import ORJSONResponse as orjson_res
from pydantic import BaseModel


class ResponseModelFactory:
    def __init__(self, status_type: str, status_code: int):
        self.status_type = status_type
        self.status_code = status_code

    def __getitem__(self, result_type):
        class ResponseModel(BaseModel):
            msg: str = self.status_type
            result: result_type
        # Class Anonymization
        class_obj = ResponseModel
        class_obj.__name__ = (
                result_type.__name__ + str(uuid4()))
        return class_obj
    
    def __call__(self, result: Any = None):
        if result:
            result = jsonable_encoder(result)
            return orjson_res(
                {'msg': self.status_type, 'result': result},
                status_code=self.status_code,
            )
        else:
            return orjson_res(
                {'msg': self.status_type},
                status_code=self.status_code,
            )


OK = ResponseModelFactory('ok', 200)

CREATED = ResponseModelFactory('created', 201)

no_content = Response(status_code=status.HTTP_204_NO_CONTENT)


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

conflict = orjson_res(
    {
        'msg': 'conflict',
        'detail': "resource already exists"
    },
    status_code=409
)


def unprocessable_entity(detail: str, errors: Optional[list] = None):
    if errors:
        body = {'msg': 'unprocessable_entity', 'detail': detail, 'errors': errors}
    else:
        body = {'msg': 'unprocessable_entity', 'detail': detail}
    return orjson_res(body, status_code=422)
