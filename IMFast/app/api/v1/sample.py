import time
from typing import Any
from fastapi import HTTPException
from app.response import OK, CREATED
from model.appmodel import Champion, ChampionCreated
from . import api


@api.get(
    '/champion',
    summary="Get Super Strong Champion",
    response_model=OK[Champion]
)
async def get_champion():
    return OK(
        Champion(
            name="Genji Shimada",
            role="Damage",
            health=200,
            affiliation="Overwatch"
        )
    )


@api.post(
    '/champion',
    summary="Create Super Strong Champion",
    response_model=CREATED[ChampionCreated],
    status_code=201,
)
async def create_champion(
    champion: Champion
):
    """ In-Out Example"""
    return CREATED(
        ChampionCreated(
            name=champion.name
        )
    )


@api.get(
    '/sample/slow',
    summary="Slow API Sample",
    response_model=OK[str]
)
async def slow():
    """It's Slow API Sample api"""
    time.sleep(1)
    return OK()


@api.post(
    '/sample/error',
    summary="Internal Error Sample",
    response_model=OK[str]
)
async def error():
    """Internal Error Sample"""
    return f"Error: {1 / 0}"


@api.put(
    '/sample/bad_request',
    summary="Bad Request Sample",
)
async def bad_request_api():
    """It's Bad Request sample api."""
    raise HTTPException(status_code=400, detail='BAD')
