from uuid import UUID

from pydantic import BaseModel, EmailStr, SecretStr


class UserSchema(BaseModel):
    email: EmailStr
    role: str


class TokenSchema(BaseModel):
    access_token: str
    refresh_token: str


class TokenPayload(BaseModel):
    sub: str = None
    exp: int = None
