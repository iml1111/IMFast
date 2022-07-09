"""JWT Dependency functions"""
from fastapi import Header, HTTPException
from controller.jwt import (
    is_refresh, is_access, get_identity)
from jose import JWTError


async def access_token(
    authorization: str = Header(...),
):
    """
    Currently, supported only Bearer Header.
    """
    token = authorization
    if token.startswith("Bearer "):
        token = token[7:]
    else:
        raise JWTError("Bearer Token is required")
    if not is_access(token):
        raise JWTError("Token is access token")
    identity = get_identity(token)
    return identity


async def refresh_token(
    authorization: str = Header(...),
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
    identity = get_identity(token)
    return identity


