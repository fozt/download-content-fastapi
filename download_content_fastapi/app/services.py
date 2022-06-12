import os.path
from urllib.parse import urljoin

import magic
from fastapi import UploadFile

from app.config import settings


def save_media(file: UploadFile) -> str:
    with open(os.path.join(settings.FILES_DIR, file.filename), "wb") as f:
        f.write(file.file.read())
    return urljoin(settings.FILES_URL, file.filename)


def get_media(filename):
    filepath = os.path.join(settings.FILES_DIR, filename)
    with open(filepath, "rb") as f:
        return {
            "content": f.read(),
            "media_type": magic.Magic(mime=True, uncompress=True).from_file(filepath),
        }
