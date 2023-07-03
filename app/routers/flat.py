import uuid
from fastapi import APIRouter
from fastapi import Depends, HTTPException, status
from config.settings import get_settings
from models.users import Flat, User

from schemas.flat import FlatSchema


settings = get_settings()
flat_router = APIRouter()


@flat_router.get("/", response_model=list[FlatSchema])
async def flats():
    return await Flat.all()


@flat_router.post("/create")
async def create_flat(form_data: FlatSchema = Depends()):
    user = await User.get_or_none(id=form_data.builder_id)
    if user:
        flat = await Flat.create(
        )
        return flat
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User not found."
        )


@flat_router.patch("/view/{flat_id}")
async def view_flat(flat_id: uuid.UUID):
    obj = await Flat.get_or_none(id=flat_id)
    if obj:
        return obj
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Flat not found."
        )


@flat_router.patch("/update/{flat_id}")
async def update_flat(flat_id: uuid.UUID, flat_schema: FlatSchema):
    obj = await Flat.get_or_none(id=flat_id)

    if obj:
        for field, value in flat_schema.dict(exclude_unset=True).items():
            setattr(obj, field, value)

        await obj.save()
        return obj
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Flat not found."
        )


@flat_router.delete("/delete/{flat_id}")
async def delete_flat(flat_id: uuid.UUID):
    obj = await Flat.get_or_none(id=flat_id)
    if obj:
        await obj.delete()
        return {"message": "Flat deleted"}
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Flat not found."
        )
