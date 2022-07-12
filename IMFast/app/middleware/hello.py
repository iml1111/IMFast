"""Declare your built-in Class Based Middleware"""
from starlette.types import ASGIApp, Receive, Scope, Send


class HelloMiddleware:
    def __init__(self, app: ASGIApp) -> None:
        self.app = app

    async def __call__(
            self,
            scope: Scope,
            receive: Receive,
            send: Send) -> None:
        await self.app(scope, receive, send)


if __name__ == '__main__':
    pass
