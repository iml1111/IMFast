"""Sample test for IMFast"""
import pytest
from httpx import AsyncClient
from loguru import logger


@pytest.mark.anyio
async def test_get_champion(client: AsyncClient):
    """Test get champion"""
    response = await client.get("/api/v1/champion")
    assert response.status_code == 200
    assert response.json()['result'] == {
        "name": "Genji Shimada",
        "role": "Damage",
        "health": 200,
        "affiliation": "Overwatch"
    }


@pytest.mark.anyio
async def test_create_champion(client: AsyncClient):
    """Test create champion"""
    response = await client.post("/api/v1/champion", json={
        "name": "D.VA",
        "role": "Tank",
        "health": 600,
        "affiliation": "Overwatch"
    })
    assert response.status_code == 201
    assert response.json()['result'] == {
        "name": "D.VA",
    }


@pytest.mark.anyio
async def test_bad_request_api(client: AsyncClient):
    """Test bad request api"""
    response = await client.put("/api/v1/sample/bad_request")
    assert response.status_code == 400
