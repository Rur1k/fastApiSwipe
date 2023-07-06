from functools import lru_cache

from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseSettings

import os

from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str
    JWT_SECRET_KEY: str
    JWT_REFRESH_SECRET_KEY: str
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
    ACCESS_TOKEN_EXPIRE_MINUTES = 30
    REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7

    class Config:
        case_sensitive: bool = True


@lru_cache()
def get_settings():
    return Settings(
        DATABASE_URL=os.getenv("DATABASE_URL"),
        SECRET_KEY=os.getenv("SECRET_KEY"),
        JWT_SECRET_KEY=os.getenv('JWT_SECRET_KEY'),
        JWT_REFRESH_SECRET_KEY=os.getenv('JWT_REFRESH_SECRET_KEY')
    )
