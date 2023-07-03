from functools import lru_cache
from pydantic import BaseSettings

import os

from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str
    APP_NAME = 'My App'
    REGISTRATION_TOKEN_LIFETIME = 60 * 60
    TOKEN_ALGORITHM = 'HS256'
    API_PREFIX = '/api'
    HOST = 'localhost'
    PORT = 8000
    BASE_URL = '{}:{}/'.format(HOST, str(PORT))
    MODELS = [
        "models.users",
        "aerich.models"
    ]

    class Config:
        case_sensitive: bool = True


@lru_cache()
def get_settings():
    return Settings(DATABASE_URL=os.getenv("DATABASE_URL"), SECRET_KEY=os.getenv("SECRET_KEY"))
