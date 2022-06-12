import os.path

from fastapi import FastAPI

from app.endpoints import api_router
from app.config import settings

app = FastAPI(openapi_url=settings.OPENAPI_PREFIX)
app.include_router(api_router)

if not os.path.exists(settings.FILES_DIR):
    os.mkdir(settings.FILES_DIR)
