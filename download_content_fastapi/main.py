import os.path

from fastapi import FastAPI

from app.endpoints import api_router

app = FastAPI(openapi_url="/openapi.json")
app.include_router(api_router)

if not os.path.exists("./data"):
    os.mkdir("./data")
