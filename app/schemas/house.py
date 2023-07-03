from uuid import UUID
from pydantic import BaseModel


class HouseSchema(BaseModel):
    name: str = None
    district: str = None
    micro_district: str = None
    street: str = None
    number: int = None
    description: str = None
    lcd_status: str = None
    type_house: str = None
    class_house: str = None
    technologies: str = None
    to_sea: str = None
    payments: str = None
    ceiling_height: str = None
    gas: str = None
    heating: str = None
    sewerage: str = None
    sales_dep_fullname: str = None
    sales_dep_phone: str = None
    sales_dep_email: str = None
    registration: str = None
    calculation_options: str = None
    appointment: str = None
    sum_in_contract: str = None
    state: str = None
    territory: str = None
    maps: str = None
    house_buildings: int = None
    sections: int = None
    floors: int = None
    risers: int = None
    builder_id: UUID = None

