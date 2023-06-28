from tortoise.models import Model
from tortoise import fields
from enum import Enum


class UserRole(str, Enum):
    ADMIN = "admin"
    BUILDER = "builder"
    USER = "user"


class User(Model):
    """User class."""
    id = fields.UUIDField(pk=True)
    username = fields.CharField(max_length=255, null=True, blank=True, unique=True)
    email = fields.CharField(db_index=True, max_length=255, unique=True)
    hashed_password = fields.CharField(null=True, max_length=255)
    phone = fields.CharField(max_length=16, null=True, blank=True)
    first_name = fields.CharField(max_length=64, default="User", blank=True)
    last_name = fields.CharField(max_length=64, default="User", blank=True)
    is_active = fields.BooleanField(default=True)
    is_staff = fields.BooleanField(default=False)
    is_blacklist = fields.BooleanField(default=False)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)
    role = fields.CharField(
        max_length=8,
        choices=[(role.value, role.name) for role in UserRole],
        default=UserRole.USER.value,
    )


class House(Model):
    id = fields.UUIDField(pk=True)
    name = fields.CharField(max_length=64, unique=True, blank=True)
    district = fields.CharField(max_length=64, null=True, blank=True)
    micro_district = fields.CharField(max_length=64, null=True, blank=True)
    street = fields.CharField(max_length=64, null=True, blank=True)
    number = fields.IntField(null=True, blank=True)
    description = fields.TextField(null=True, blank=True)
    lcd_status = fields.CharField(max_length=64, null=True, blank=True)
    type_house = fields.CharField(max_length=64, null=True, blank=True)
    class_house = fields.CharField(max_length=64, null=True, blank=True)
    technologies = fields.CharField(max_length=64, null=True, blank=True)
    to_sea = fields.CharField(max_length=64, null=True, blank=True)
    payments = fields.CharField(max_length=64, null=True, blank=True)
    ceiling_height = fields.CharField(max_length=64, null=True, blank=True)
    gas = fields.CharField(max_length=64, null=True, blank=True)
    heating = fields.CharField(max_length=64, null=True, blank=True)
    sewerage = fields.CharField(max_length=64, null=True, blank=True)
    sales_dep_fullname = fields.CharField(max_length=128, null=True, blank=True)
    sales_dep_phone = fields.CharField(max_length=16, null=True, blank=True)
    sales_dep_email = fields.CharField(max_length=64, null=True, blank=True)
    registration = fields.TextField(null=True, blank=True)
    calculation_options = fields.TextField(null=True, blank=True)
    appointment = fields.TextField(max_length=64, null=True, blank=True)
    sum_in_contract = fields.TextField(max_length=64, null=True, blank=True)
    state = fields.CharField(max_length=64, null=True, blank=True)
    territory = fields.CharField(max_length=64, null=True, blank=True)
    maps = fields.TextField(null=True, blank=True)
    house_buildings = fields.IntField(null=True, blank=True)
    sections = fields.IntField(null=True, blank=True)
    floors = fields.IntField(null=True, blank=True)
    risers = fields.IntField(null=True, blank=True)
    builder = fields.ForeignKeyField("users.User", on_delete=fields.CASCADE, null=True, blank=True)


class Flat(Model):
    id = fields.UUIDField(pk=True)
    number = fields.IntField(null=True, blank=True)
    house = fields.ForeignKeyField("users.House", on_delete=fields.CASCADE, null=True, blank=True)
    count_room = fields.IntField(null=True, blank=True)
    square = fields.FloatField(null=True, blank=True)
    price_per_meter = fields.FloatField(null=True, blank=True)
    house_building = fields.IntField(null=True, blank=True)
    section = fields.IntField(null=True, blank=True)
    floor = fields.IntField(null=True, blank=True)
    riser = fields.IntField(null=True, blank=True)
    creator = fields.ForeignKeyField("users.User", on_delete=fields.CASCADE, null=True, blank=True)
    reserved = fields.BooleanField(default=False, blank=True)


class Notary(Model):
    id = fields.UUIDField(pk=True)
    first_name = fields.CharField(max_length=64, null=True, blank=True)
    last_name = fields.CharField(max_length=64, null=True, blank=True)
    phone = fields.CharField(max_length=16, null=True, blank=True)
    email = fields.CharField(max_length=64, null=True, blank=True)


class Announcement(Model):
    id = fields.UUIDField(pk=True)
    user = fields.ForeignKeyField("users.User", on_delete=fields.CASCADE, null=True, blank=True)
    house = fields.ForeignKeyField("users.House", on_delete=fields.CASCADE, null=True, blank=True)
    founding_documents = fields.CharField(max_length=64, null=True, blank=True)
    purpose = fields.CharField(max_length=64, null=True, blank=True)
    count_rooms = fields.CharField(max_length=64, null=True, blank=True)
    layout = fields.CharField(max_length=64, null=True, blank=True)
    residential_condition = fields.CharField(max_length=64, null=True, blank=True)
    all_square = fields.FloatField(default=0, null=True, blank=True)
    balcony = fields.BooleanField(default=False, null=True, blank=True)
    heating_type = fields.CharField(max_length=64, null=True, blank=True)
    commission_to_agent = fields.FloatField(default=0, null=True, blank=True)
    connection_type = fields.CharField(max_length=64, null=True, blank=True)
    description = fields.TextField(null=True, blank=True)
    price = fields.FloatField(null=True, blank=True)
    calculation_option = fields.CharField(max_length=64, null=True, blank=True)
    maps = fields.TextField(null=True, blank=True)
    pub_status = fields.BooleanField(default=False, null=True, blank=True)


class Favorite(Model):
    id = fields.UUIDField(pk=True)
    user = fields.ForeignKeyField("users.User", on_delete=fields.CASCADE, null=True, blank=True)
    announcement = fields.ForeignKeyField("users.Announcement", on_delete=fields.CASCADE, null=True, blank=True)
