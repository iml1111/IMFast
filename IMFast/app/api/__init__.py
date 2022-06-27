"""
ref: https://fastapi.tiangolo.com/tutorial/middleware/
# FIXME check https://stackoverflow.com/questions/60098005/fastapi-starlette-get-client-real-ip
"""
import time
from typing import Callable
from fastapi import FastAPI, Request
from loguru import logger
from settings import settings


def init_app(app: FastAPI):
    """Declare your built-in Functional Middleware"""

    @app.on_event("startup")
    async def startup():
        """run before the application starts"""

    @app.on_event("shutdown")
    async def shutdown():
        """run when the application is shutting down"""

    @app.middleware("http")
    async def slow_api_tracker(
            request: Request,
            call_next: Callable):
        
        process_time = time.time()
        response = await call_next(request)
        process_time = time.time() - process_time

        if process_time >= settings.slow_api_time:
            log_str = (
                f"\n!!! SLOW API DETECTED !!!\n"
                f"ip: {request.client.host}\n"
                f"url: {request.url.path}\n"
                # TODO 이상한 코루틴 객체가 온다?
                f"input_body: {request.body()}\n"
                f"slow time: {process_time}")
            logger.error(log_str)

        return response

    @app.middleware('http')
    async def hello_func_middleware(
            request: Request,
            call_next: Callable):
        """executed before slow_api_tracker"""
        return await call_next(request)
