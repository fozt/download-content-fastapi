from typing import List, Optional

from fastapi import APIRouter, Form, UploadFile
from fastapi.responses import Response

from app.db import get_all, insert_file
from app.schemas import ContentRead
from app.services import get_media, save_media

api_router = APIRouter(prefix="/downloader")


@api_router.post("/", response_model=ContentRead)
def upload_content(
    musicFile: UploadFile,
    coverFile: UploadFile,
    title: str = Form(),
    description: str = Form(default=""),
):
    content = ContentRead(
        coverUrl=save_media(coverFile),
        musicUrl=save_media(musicFile),
        coverFileName=coverFile.filename,
        musicFileName=musicFile.filename,
        title=title,
        description=description,
    )
    insert_file(content)
    return content


@api_router.get("/", response_model=Optional[List[ContentRead]])
def get_all_contents():
    return get_all()


@api_router.get("/{filename}")
def get_content(filename: str):
    return Response(**get_media(filename))
