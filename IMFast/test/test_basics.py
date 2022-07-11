from typing import Callable
from fastapi import FastAPI
from httpx import AsyncClient
import pytest

from test.fixture import app, client

# TODO 전체 셋업/티어다운 가능?


def setup_function(function: Callable):
    """
    setup any state tied to the execution of the given function.
    Invoked for every test function in the module.
    """
    # TODO What is this?


def teardown_function(function: Callable):
    """
    setup any state tied to the execution of the given function.
    Invoked for every test function in the module.
    """
    # TODO What is this?


def test_app_exists(app: FastAPI):
    """Test app exists"""
    assert (app is not None)


@pytest.mark.anyio
async def test_index_page(client: AsyncClient):
    """Test index page"""
    response = await client.get("/")
    assert response.status_code == 200


@pytest.mark.anyio
async def test_404_page(client: AsyncClient):
    """Test 404 page"""
    response = await client.get("/404")
    assert response.status_code == 404
