from uuid import UUID
from pydantic import BaseModel


class AnnouncementSchema(BaseModel):
    user_id: UUID
    house_id: UUID
    founding_documents: str
    purpose: str
    count_rooms: str
    layout: str
    residential_condition: str
    all_square: float
    balcony: bool
    heating_type: str
    commission_to_agent: float
    connection_type: str
    description: str
    price: float
    calculation_option: str
    maps: str
    pub_status: bool

