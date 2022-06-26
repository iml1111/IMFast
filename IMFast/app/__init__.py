from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from settings import Settings, __VERSION__
from app import api
from app.middleware import GlobalsMiddleware
import model


def create_app(settings: Settings) -> FastAPI:
    """Applcation Factory"""
    app = FastAPI(
        title=settings.app_name,
        description=settings.description,
        version=__VERSION__,
        docs_url=settings.docs_url,)

    # Built-in init
    settings.init_app(app)
    model.init_app(app, settings)

    # Extension/Middleware init
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )
    app.add_middleware(GlobalsMiddleware)
    # TODO GZipMiddleware
    # TODO TrustedHostMiddleware
    # TODO HTTPS RedirectMiddleWare ?
    # https://fastapi.tiangolo.com/ko/advanced/middleware/

    # Register Routers

    return app