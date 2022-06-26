from contextvars import ContextVar, Token
from typing import Any, Dict
from starlette.types import ASGIApp, Receive, Scope, Send


class Globals:
    __slots__ = ("_vars", "_reset_tokens")

    _vars: Dict[str, ContextVar]
    _reset_tokens: Dict[str, Token]

    def __init__(self) -> None:
        object.__setattr__(self, '_vars', {})
        object.__setattr__(self, '_reset_tokens', {})

    def reset(self) -> None:
        # FIXME reset에 대한 오버헤드가 우려됨
        for _name, var in self._vars.items():
            try:
                var.reset(self._reset_tokens[_name])
            except ValueError:
                var.set(None)

    def _ensure_var(self, item: str) -> None:
        if item not in self._vars:
            self._vars[item] = ContextVar(f"globals:{item}", default=None)
            self._reset_tokens[item] = self._vars[item].set(None)

    def __getattr__(self, item: str) -> Any:
        self._ensure_var(item)
        return self._vars[item].get()

    def __setattr__(self, item: str, value: Any) -> None:
        self._ensure_var(item)
        self._vars[item].set(value)

    def __contains__(self, item) -> bool:
        return item in self._vars


class GlobalsMiddleware:
    def __init__(self, app: ASGIApp) -> None:
        self.app = app

    async def __call__(
            self,
            scope: Scope,
            receive: Receive,
            send: Send) -> None:
        g.reset()
        await self.app(scope, receive, send)


g = Globals()
# FIXME 삭제 예정 helo Middleware로 대체

if __name__ == '__main__':
    pass