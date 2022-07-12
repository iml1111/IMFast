"""
Basic Test for the API
"""
import pytest
from fastapi import FastAPI
from httpx import AsyncClient
from loguru import logger


def test_app_exists(app: FastAPI):
    """Test app exists"""
    assert app is not None


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
