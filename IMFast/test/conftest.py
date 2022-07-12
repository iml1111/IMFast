import logging
from fastapi import FastAPI
from loguru import logger
from pytest import fixture
import pytest
from app import create_app
from httpx import AsyncClient
from settings import settings

# external fixtures
from _pytest.logging import caplog as _caplog


@fixture(scope='session')
def app() -> FastAPI:
    """
    Create a FastAPI application for the tests.
    """
    app: FastAPI = create_app(settings)
    return app


@fixture
async def client(app: FastAPI) -> AsyncClient:
    """
    Create a test client for the FastAPI application.
    """
    async with AsyncClient(
            app=app,
            base_url="http://localhost:5000") as ac:
        yield ac


@fixture(autouse=True)
def caplog(_caplog):
    """Overiding pytest-capturelog's caplog fixture."""
    class PropagatingLogger(logging.Handler):
        def emit(self, record):
            logging.getLogger(record.name).handle(record)

    handler_id = logger.add(
        PropagatingLogger(),
        format="{message} {extra}",
        level="DEBUG")
    yield _caplog
    # After the test, remove the handler again
    logger.remove(handler_id)
