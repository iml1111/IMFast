import logging
from fastapi import FastAPI
from loguru import logger
import pytest
from app import create_app
from httpx import AsyncClient
from settings import TestSettings

# external fixtures
from _pytest.logging import caplog as _caplog


@pytest.fixture(scope='session')
def anyio_backend():
    return 'asyncio'


@pytest.fixture
def app() -> FastAPI:
    """
    Create a FastAPI application for the tests.
    """
    settings = TestSettings()
    app: FastAPI = create_app(settings)
    return app


@pytest.fixture
async def client(app: FastAPI) -> AsyncClient:
    """
    Create a test client for the FastAPI application.
    """
    async with AsyncClient(
            app=app,
            base_url="http://localhost:5000") as ac:
        yield ac


@pytest.fixture(autouse=True)
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
