from typing import List, Optional

from fastapi import APIRouter, Form, HTTPException, Response, UploadFile, status

from app.db import get_all, insert_file
from app.schemas import ContentInDB, ContentRead
from app.services import get_media, save_media

api_router = APIRouter(prefix="/downloader")


@api_router.post("/", response_model=ContentRead)
def upload_content(
    musicFile: UploadFile,
    coverFile: UploadFile,
    title: str = Form(),
    description: str = Form(default=""),
):
    save_media(coverFile)
    save_media(musicFile)
    content = ContentInDB(
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
    try:
        return Response(**get_media(filename))
    except FileNotFoundError:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND)
