import traceback
from fastapi import Request, FastAPI, HTTPException
from fastapi.responses import ORJSONResponse
from app.response import bad_request, not_found
from loguru import logger

def init_app(app: FastAPI):

    @app.exception_handler(400)
    async def bad_request_handler(
            request: Request,
            exc: HTTPException):
        return bad_request(exc.detail)

    @app.exception_handler(404)
    async def not_found_handler(
            request: Request,
            exc: HTTPException):
        return not_found

    @app.exception_handler(500)
    async def internal_server_error_handler(
            request: Request,
            exc: HTTPException):
        return ORJSONResponse(
            {'msg': 'internal_server_error'},
            status_code=500,
        )