from tinydb import TinyDB

from app.schemas import ContentRead

db = TinyDB("db.json")


def insert_file(content: ContentRead):
    db.insert(content.dict())


def get_all():
    return [ContentRead.parse_obj(obj) for obj in db.all()]
