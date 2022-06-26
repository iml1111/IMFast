"""
TODO 스크림트 매니저
스크립트 매니지먼트 툴이 없는거 같은데? 클릭이 있는데?
쉘스크립트로 추가해보자. (imfast),
https://fastapi.tiangolo.com/ko/deployment/server-workers/
"""
from app import create_app
from settings import settings


application = create_app(settings)