from uuid import uuid4
from datetime import datetime, timedelta
from jose import JWTError, jwt


def create_access_token(
    data, *,
    expires_delta: int,
    secret_key: str,
    algorithm: str,
) -> str:
    return _create_token(
        data,
        'access',
        expires_delta,
        secret_key,
        algorithm
    )


def create_refresh_token(
    data, *,
    expires_delta: int,
    secret_key: str,
    algorithm: str,
) -> str:
    return _create_token(
        data,
        'refresh',
        expires_delta,
        secret_key,
        algorithm
    )


def get_identity(
    token: str, *,
    secret_key: str,
    algorithm: str,
):
    payload = _decode_token(
        token, secret_key=secret_key, algorithm=algorithm)
    identity = payload.get('sub')
    if identity is None:
        raise JWTError('No subject claim in the JWT payload')
    return identity


def is_access(
    token: str, *,
    secret_key: str,
    algorithm: str,
):
    payload = _decode_token(
        token, secret_key=secret_key, algorithm=algorithm)
    return payload.get('type') == 'access'


def is_refresh(
    token: str, *,
    secret_key: str,
    algorithm: str,
):
    payload = _decode_token(
        token, secret_key=secret_key, algorithm=algorithm)
    return payload.get('type') == 'refresh'


def get_raw_token(
    token: str, *,
    secret_key: str,
    algorithm: str,
):
    return _decode_token(
        token, secret_key=secret_key, algorithm=algorithm)


def _decode_token(
    token: str, *,
    secret_key: str,
    algorithm: str,
):
    return jwt.decode(
        token, secret_key,
        algorithms=[algorithm],
        # available any object in sub field.
        options={'verify_sub': False},
    )


def _create_token(
    data,
    token_type: str,
    expires_delta: int,
    secret_key: str,
    algorithm: str,
) -> str:
    now_time = datetime.utcnow()
    to_encode = {
        'jti': str(uuid4()),
        'type': token_type,
        'sub': data,
        'iat': now_time,
        'nbf': now_time,
        'exp': now_time + timedelta(seconds=expires_delta),
    }
    token = jwt.encode(to_encode, secret_key, algorithm=algorithm)
    return token
