from pydantic import BaseModel


class ContentRead(BaseModel):
    musicFileName: str
    coverFileName: str
    musicUrl: str
    coverUrl: str
    title: str
    description: str
