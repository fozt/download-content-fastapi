from urllib.parse import urljoin

from pydantic import BaseModel, root_validator

from app.config import settings


class ContentInDB(BaseModel):
    musicFileName: str
    coverFileName: str
    title: str
    description: str


class ContentRead(ContentInDB):
    musicUrl: str = ""
    coverUrl: str = ""

    @root_validator
    def setMusicUrl(cls, values):
        values["musicUrl"] = urljoin(settings.FILES_URL, values["musicFileName"])
        values["coverUrl"] = urljoin(settings.FILES_URL, values["coverFileName"])
        return values
