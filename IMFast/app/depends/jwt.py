"""JWT Dependency functions"""
from fastapi import Header, Depends
from controller.jwt import (
    is_refresh, is_access, get_identity
)
from app.depends.module import app_settings
from jose import JWTError
from settings import Settings


async def access_token(
    authorization: str = Header(...),
    settings: Settings = Depends(app_settings)
):
    """
    Currently, supported only Bearer Header.
    """
    token = authorization
    if token.startswith("Bearer "):
        token = token[7:]
    else:
        raise JWTError("Bearer Token is required")
    if not is_access(
        token,
        secret_key=settings.secret_key,
        algorithm=settings.algorithm
    ):
        raise JWTError("Token is access token")
    identity = get_identity(token)
    return identity


async def refresh_token(
    authorization: str = Header(...),
    settings: Settings = Depends(app_settings)
):
    """
    Currently, supported only Bearer Header.
    """
    token = authorization
    if token.startswith("Bearer "):
        token = token[7:]
    else:
        raise JWTError("Bearer Token is required")
    if not is_refresh(token):
        raise JWTError("Token is not refresh token")
    identity = get_identity(
        token,
        secret_key=settings.secret_key,
        algorithm=settings.algorithm
    )
    return identity


