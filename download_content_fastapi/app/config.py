from pydantic import BaseSettings


class Settings(BaseSettings):
    FILES_URL: str
    FILES_PATH: str


settings = Settings()
