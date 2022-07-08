import os
from pydantic import BaseSettings, Field
from fastapi import FastAPI

__AUTHOR__ = "IML"
__VERSION__ = "0.1.1"

APP_NAME = "IMFast"
BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Settings(BaseSettings):
    # Description settings
    app_name: str = Field(APP_NAME, env='APP_NAME')
    description: str = "Welcome to IMFast."
    term_of_service: str = "https://github.com/iml1111"
    contact_name: str = __AUTHOR__
    contact_url: str = "https://github.com/iml1111"
    contact_email: str = "shin10256@gmail.com"
    # Documentation url
    docs_url: str = "/docs"

    secret_key: str = "super-secret"
    slow_api_time: float = 0.5

    class Config:
        env_prefix = f"{APP_NAME.upper()}_"
        # TODO: 어떻게 env 파일을 분리시켜 관리할 수 있을까
        env_file = '.env'
        env_file_encoding = 'utf-8'

    def init_app(self, app: FastAPI):
        ...


settings = Settings()


if __name__ == '__main__':
    print(settings.dict())
    print(BASE_DIR)