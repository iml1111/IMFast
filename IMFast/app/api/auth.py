from fastapi import APIRouter, Body, Header
from app.response import ok
from controller.jwt import create_access_token, create_refresh_token

auth = APIRouter()


@auth.post(
    "/sign-in",
    summary='SignIn',
    tags=['auth'],
)
async def login(
    username: str = Body(...),
    password: str = Body(...),
):
    """
    Login API
    """
    if username == "admin" and password == "admin":
        return ok({
            "message": "Login Success",
            "access_token": create_access_token(username),
            "refresh_token": create_refresh_token(username)
        })
    else:
        return ok({"message": "Login Failed"})


@auth.post(
    "/refresh",
    summary="Token Refresh",
    tags=['auth']
)
async def refresh(
    authorization: str = Header(...),
):
    """
    Refresh Token API
    """
    from loguru import logger
    logger.info(authorization)
    return ok()