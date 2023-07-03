from pydantic import BaseModel, EmailStr


class NotarySchema(BaseModel):
    first_name: str
    last_name: str
    phone: str
    email: EmailStr

