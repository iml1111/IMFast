"""
ref: https://fastapi.tiangolo.com/tutorial/middleware/
# FIXME check https://stackoverflow.com/questions/60098005/fastapi-starlette-get-client-real-ip
"""
import time
from typing import Callable
from fastapi import FastAPI, Request
from settings import settings
from app.middleware import g


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
        response = await call_next(request)

        if (
            'process_time' in g
            and g.process_time >= settings.slow_api_time
        ):

            log_str = (
                f"!!! SLOW API DETECTED !!!\n"
                f"ip: {request.client.host}\n"
                f"url: {request.url.path}\n"
                f"input_body: {request.body()}\n"
                f"slow time: {g.process_time}"
            )

        return response