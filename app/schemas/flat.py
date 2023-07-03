from uuid import UUID
from pydantic import BaseModel


class FlatSchema(BaseModel):
    number: int
    house_id: UUID
    count_room: int
    square: float
    price_per_meter: float
    house_building: int
    section: int
    floor: int
    riser: int
    creator_id: UUID
    reserved: bool

