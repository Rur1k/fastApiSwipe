import asyncio
import random

from tortoise.expressions import F

from services.auth import Auth
from models.users import User, House, Flat, Announcement, Notary, Favorite
from faker import Faker

fake = Faker()


async def populate_data():
    # create superuser
    if await User.filter(is_active=True, is_staff=True, role="admin").count() == 0:
        admin = await User.create(
            email="admin@admin.com",
            hashed_password=Auth.get_password_hash("admin"),
            is_staff=True,
            role="admin"
        )
        await admin.save()

    # create builder
    if await User.filter(is_active=True, role="builder").count() == 0:
        for i in range(3):
            builder = await User.create(
                email=f"builder{i}@builder.com",
                hashed_password=Auth.get_password_hash("builder"),
                role="builder"
            )
            await builder.save()

    # create house
    if await House.all().count() == 0:
        for builder in await User.filter(role="builder"):
            for i in range(5):
                house = await House.create(
                    name=f"{builder.first_name} -  house {i}",
                    district=f"district - {i}",
                    micro_district=f"micro_district - {i}",
                    street=fake.street_address(),
                    number=i,
                    description=f"description - {i}",
                    lcd_status=f"lcd_status - {i}",
                    type_house=f"type_house - {i}",
                    class_house=f"class_house - {i}",
                    technologies=f"technologies - {i}",
                    to_sea=f"to_sea - {i}",
                    payments=f"payments - {i}",
                    ceiling_height=f"ceiling_height - {i}",
                    gas=f"gas - {i}",
                    heating=f"heating - {i}",
                    sewerage=f"sewerage - {i}",
                    sales_dep_fullname=f"sales_dep_fullname - {i}",
                    sales_dep_phone=f"093000000{i}",
                    sales_dep_email=f"sales_dep_email - {i}",
                    registration=f"registration - {i}",
                    calculation_options=f"calculation_options - {i}",
                    appointment=f"appointment - {i}",
                    sum_in_contract=f"sum_in_contract - {i}",
                    state=f"state - {i}",
                    territory=f"territory - {i}",
                    maps=f"maps - {i}",
                    house_buildings=i,
                    sections=2,
                    floors=10,
                    risers=4,
                    builder=builder
                )
                await house.save()

    # create flat
    if await Flat.all().count() == 0:
        for house in await House.all():
            for i in range(5):
                flat = await Flat.create(
                    number=i,
                    house=house,
                    count_room=random.randint(1, 5),
                    square=random.randint(20, 100),
                    price_per_meter=random.randint(20, 50),
                    house_building=i,
                    section=random.randint(1, 2),
                    floor=random.randint(1, 10),
                    riser=random.randint(1, 2),
                    creator=await User.filter().first().offset(int(await User.all().count() * random.random()))
                )

    # create notary
    if await Notary.all().count() == 0:
        for i in range(10):
            await Notary.create(
                first_name=fake.last_name(),
                last_name=fake.first_name(),
                phone=f"093000000{i}",
                email=fake.email()
            )

    # create announcement
    if await Announcement.all().count() == 0:
        for house in await House.all():
            for i in range(10):
                await Announcement.create(
                    user=await User.filter().first().offset(int(await User.all().count() * random.random())),
                    house=house,
                    founding_documents=f"founding_documents - {i}",
                    purpose=f"purpose - {i}",
                    count_rooms=random.randint(1, 5),
                    layout=f"layout - {i}",
                    residential_condition=f"residential_condition - {i}",
                    all_square=random.randint(20, 100),
                    balcony=True,
                    heating_type=f"heating_type - {i}",
                    commission_to_agent=random.randint(10, 20),
                    connection_type=f"connection_type - {i}",
                    description=f"description - {i}",
                    price=random.randint(1000, 9999),
                    calculation_option=f"calculation_option - {i}",
                    maps=f"maps - {i}",
                    pub_status=True
                )
