from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

def create_app(config) -> FastAPI:
	"""Applcation Factory"""
	app = FastAPI(
		title=config.APP_NAME,
		description=config.APP_DESCRIPTION,
        version=config.APP_VERSION,
		docs_url=config.DOCS_URL,)

	app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )

	return app