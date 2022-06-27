from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from fastapi.middleware.cors import CORSMiddleware
from settings import Settings, __VERSION__
from app import api
from app.middleware import HelloMiddleware
import model

from app.api.template import api as template
from app.api.v1 import api as api_v1


def create_app(settings: Settings) -> FastAPI:
    """Application Factory"""
    app = FastAPI(
        title=settings.app_name,
        description=settings.description,
        version=__VERSION__,
        docs_url=settings.docs_url,
        default_response_class=ORJSONResponse
    )

    # Built-in init
    settings.init_app(app)
    api.init_app(app)
    model.init_app(app, settings)

    # Extension/Middleware init
    app.add_middleware(
        CORSMiddleware,
        allow_credentials=True,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"]
    )
    app.add_middleware(HelloMiddleware)
    # TODO GZipMiddleware
    # TODO TrustedHostMiddleware
    # TODO HTTPS RedirectMiddleWare ?
    # https://fastapi.tiangolo.com/ko/advanced/middleware/

    # Register Routers
    app.include_router(template)
    app.include_router(api_v1, prefix='/api/v1')

    return app