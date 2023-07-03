from pydantic import BaseModel, EmailStr, SecretStr


class UserCreate(BaseModel):
    email: EmailStr
    password: str
    repeat_password: str
