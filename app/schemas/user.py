from uuid import UUID

from pydantic import BaseModel


class BuilderSchema(BaseModel):
    id: UUID
    email: str
    phone: str
    first_name: str
    last_name: str
