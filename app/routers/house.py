import uuid

from fastapi import APIRouter
from fastapi import Depends, HTTPException, status
from config.settings import get_settings
from models.users import House

from schemas.house import HouseSchema

from models.users import User

settings = get_settings()
house_router = APIRouter()


@house_router.get("/", response_model=list[HouseSchema])
async def houses():
    return await House.all()


@house_router.post("/create")
async def create_house(form_data: HouseSchema = Depends()):
    user = await User.get_or_none(id=form_data.builder_id)
    if user:
        house = await House.create(
            name=form_data.name,
            district=form_data.district,
            micro_district=form_data.micro_district,
            street=form_data.street,
            number=form_data.number,
            description=form_data.description,
            lcd_status=form_data.lcd_status,
            type_house=form_data.type_house,
            class_house=form_data.class_house,
            technologies=form_data.technologies,
            to_sea=form_data.to_sea,
            payments=form_data.payments,
            ceiling_height=form_data.ceiling_height,
            gas=form_data.gas,
            heating=form_data.heating,
            sewerage=form_data.sewerage,
            sales_dep_fullname=form_data.sales_dep_fullname,
            sales_dep_phone=form_data.sales_dep_phone,
            sales_dep_email=form_data.sales_dep_email,
            registration=form_data.registration,
            calculation_options=form_data.calculation_options,
            appointment=form_data.appointment,
            sum_in_contract=form_data.sum_in_contract,
            state=form_data.state,
            territory=form_data.territory,
            maps=form_data.maps,
            house_buildings=form_data.house_buildings,
            sections=form_data.sections,
            floors=form_data.floors,
            risers=form_data.risers,
            builder=user
        )
        return house
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User not found."
        )


@house_router.patch("/view/{house_id}")
async def view_house(house_id: uuid.UUID):
    obj = await House.get_or_none(id=house_id)
    if obj:
        return obj
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="House not found."
        )


@house_router.patch("/update/{house_id}")
async def update_house(house_id: uuid.UUID, house_schema: HouseSchema):
    obj = await House.get_or_none(id=house_id)

    if obj:
        for field, value in house_schema.dict(exclude_unset=True).items():
            setattr(obj, field, value)

        await obj.save()
        return obj
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="House not found."
        )


@house_router.delete("/delete/{house_id}")
async def delete_house(house_id: uuid.UUID):
    obj = await House.get_or_none(id=house_id)
    if obj:
        await obj.delete()
        return {"message": "House deleted"}
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="House not found."
        )
