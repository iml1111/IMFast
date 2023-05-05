import time
from typing import Callable
from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from loguru import logger
from app.response import unprocessable_content
from settings import settings, Settings
import model


def init_app(
        app: FastAPI,
        app_settings: Settings):
    """Declare your built-in Functional Middleware"""

    @app.on_event("startup")
    async def startup():
        """run before the application starts"""
        model.init_app(app, app_settings)

    @app.on_event("shutdown")
    async def shutdown():
        """run when the application is shutting down"""

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request, exc: RequestValidationError):
        """Validation Exception Handler"""
        errors: list = exc.errors()
        detail = errors[0].get('msg') if errors else None
        return unprocessable_content(detail, errors)

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
            log_str: str = (
                f"\n!!! SLOW API DETECTED !!!\n"
                f"time: {process_time}\n"
                f"url: {request.url.path}\n"
                f"ip: {request.client.host}\n")
            logger.error(log_str)

        return response

    @app.middleware('http')
    async def hello_func_middleware(
            request: Request,
            call_next: Callable):
        """executed before slow_api_tracker"""
        return await call_next(request)
