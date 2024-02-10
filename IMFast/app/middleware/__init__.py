import time
from urllib.parse import urlsplit
from typing import Callable
from fastapi import FastAPI, Request
from loguru import logger
from settings import Settings
import model

# Class-based Middleware
from .hello import HelloMiddleware


def init_app(
    app: FastAPI,
    app_settings: Settings
):
    """Declare your built-in Functional Middleware"""
    @app.middleware("http")
    async def slow_api_tracker(
            request: Request,
            call_next: Callable):
        """slow api tracker middleware"""
        
        process_time = time.time()
        response = await call_next(request)
        process_time = time.time() - process_time
        response.headers["X-Process-Time"] = str(process_time)

        if process_time >= app_settings.slow_api_time:
            request_url = urlsplit(request.url._url)
            log_str: str = (
                f"\n!!! SLOW API DETECTED !!!\n"
                f"time: {process_time}\n"
                f"url: [{request.method}] {request_url.path}"
                f"{'?' + request_url.query if request_url.query else ''}\n"
                f"ip: {request.client.host}\n")
            logger.error(log_str)

        return response

    @app.middleware('http')
    async def hello_func_middleware(
            request: Request,
            call_next: Callable):
        """executed before slow_api_tracker"""
        return await call_next(request)