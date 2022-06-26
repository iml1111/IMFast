from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from settings import Settings, __VERSION__

def create_app(settings: Settings) -> FastAPI:
	"""Applcation Factory"""
	app = FastAPI(
		title=settings.app_name,
		description=settings.description,
        version=__VERSION__,
		docs_url=settings.docs_url,)

	app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )

	return app