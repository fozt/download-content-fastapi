import os.path

from fastapi import FastAPI

from app.config import settings
from app.endpoints import api_router

app = FastAPI(openapi_url=settings.OPENAPI_PREFIX)
app.include_router(api_router)

try:
    os.mkdir(settings.FILES_DIR)
except FileExistsError:
    pass
