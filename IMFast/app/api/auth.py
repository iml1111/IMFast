from fastapi import APIRouter, Body, Depends
from app.depends import refresh_token, access_token, app_settings
from app.response import OK
from controller.jwt import create_access_token, create_refresh_token
from settings import Settings

auth = APIRouter()


@auth.post(
    "/signin",
    summary='SignIn',
    tags=['auth'],
)
async def login(
    username: str = Body(...),
    password: str = Body(...),
    settings: Settings = Depends(app_settings)
):
    """
    Login API
    """
    if username == "admin" and password == "admin":
        return OK({
            "message": "Login Success",
            "access_token": create_access_token(
                username,
                expires_delta=settings.access_token_expire,
                secret_key=settings.secret_key,
                algorithm=settings.algorithm
            ),
            "refresh_token": create_refresh_token(
                username,
                expires_delta=settings.refresh_token_expire,
                secret_key=settings.secret_key,
                algorithm=settings.algorithm
            )
        })
    else:
        return OK({"message": "Login Failed"})


@auth.post(
    "/refresh",
    summary="Token Refresh",
    tags=['auth']
)
async def refresh(
    identity: str = Depends(refresh_token),
    settings: Settings = Depends(app_settings)
):
    """
    Refresh Token API
    """
    return OK({
        "message": "Refresh Success",
        "access_token": create_access_token(
            identity,
            expires_delta=settings.access_token_expire,
            secret_key=settings.secret_key,
            algorithm=settings.algorithm
        ),
        "refresh_token": create_refresh_token(
            identity,
            expires_delta=settings.refresh_token_expire,
            secret_key=settings.secret_key,
            algorithm=settings.algorithm
        )
    })


@auth.get(
    "/me",
    summary="Get User Info",
    tags=['auth']
)
async def me(
    identity: str = Depends(access_token),
):
    """
    Get User Info API
    """
    return OK({
        "message": "Get User Info Success",
        "username": identity
    })