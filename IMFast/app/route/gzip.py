from typing import Callable
from fastapi import Response, Request
from fastapi.routing import APIRoute
from app.request import GzipRequest


class GzipRoute(APIRoute):
    def get_route_handler(self) -> Callable:
        original_route_handler = super().get_route_handler()
        async def custom_route_handler(request: Request) -> Response:
            request = GzipRequest(request.scope, request.receive)
            return await original_route_handler(request)
        return custom_route_handler
