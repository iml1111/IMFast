import time
from typing import Callable
from fastapi import FastAPI, Request
from loguru import logger
from starlette_context import context
from settings import settings, Settings
import model
from app import error_handler


def init_app(
        app: FastAPI,
        app_settings: Settings):
    """Declare your built-in Functional Middleware"""

    @app.on_event("startup")
    async def startup():
        """run before the application starts"""
        model.init_app(app, app_settings)
        error_handler.init_app(app)

    @app.on_event("shutdown")
    async def shutdown():
        """run when the application is shutting down"""

    @app.middleware("http")
    async def slow_api_tracker(
            request: Request,
            call_next: Callable):
        """slow api tracker middleware"""
        
        process_time = time.time()
        response = await call_next(request)
        process_time = time.time() - process_time
        response.headers["X-Process-Time"] = str(process_time)

        if process_time >= settings.slow_api_time:
            # Get body in the ContextMiddleware
            request_body = context.get('body')
            log_str: str = (
                f"\n!!! SLOW API DETECTED !!!\n"
                f"time: {process_time}\n"
                f"url: {request.url.path}\n"
                f"ip: {request.client.host}\n")
            log_str += f"body: {str(request_body)}\n"
            logger.error(log_str)

        return response

    @app.middleware('http')
    async def hello_func_middleware(
            request: Request,
            call_next: Callable):
        """executed before slow_api_tracker"""
        return await call_next(request)
