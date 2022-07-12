"""
If you want to make appmodel code, I suggest jsonable_encoder
"""
from fastapi import FastAPI
from settings import Settings


def init_app(app: FastAPI, setting: Settings):
    pass