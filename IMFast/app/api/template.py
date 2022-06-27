from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from settings import settings, BASE_DIR

api = APIRouter()
template_engine = Jinja2Templates(
    directory=f"{BASE_DIR}/app/asset")
template = template_engine.TemplateResponse


@api.get('/')
async def index(request: Request):
    return template(
        'index.html',
        context={
            'request': request,
            'description': settings.description
        }
    )
