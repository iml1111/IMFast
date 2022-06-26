import os
from pydantic import BaseSettings, Field, validator
from fastapi import FastAPI

__AUTHOR__ = "IML"
__VERSION__ = "0.1.1"
APP_NAME = "IMFast"


class Settings(BaseSettings):
    # all configs auto-detect OS Env vars.
    app_name: str = Field(APP_NAME, env='APP_NAME')
    description: str = "Welcome to IMFast."
    docs_url: str = "/api-spec"
    secret_key: str = "super-secret"
    slow_api_time: float = 0.5
    timer_output: str = "response"

    class Config:
        env_prefix = f"{APP_NAME.upper()}_"

    def init_app(self, app: FastAPI):
        ...

    @validator('timer_output')
    def response_or_log(cls, v):
        if v not in ('response', 'log'):
            raise ValueError(
                "'timer_output' must be in ('response', 'log')")
        return v


# TODO: 어떻게 env 파일을 편리하게 분리시켜 관리할 수 있을까
settings = Settings(
    _env_file='.env', # your env file path
    _env_file_encoding='utf-8')


if __name__ == '__main__':
    print(settings.dict())