"""
TODO 스크립트 매니저
"""
from app import create_app
from settings import settings


application = create_app(settings)
