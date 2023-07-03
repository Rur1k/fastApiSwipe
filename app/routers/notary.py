from fastapi import APIRouter
from fastapi import Depends, HTTPException, status
from config.settings import get_settings
from models.users import Notary

from schemas.notary import NotarySchema

settings = get_settings()
notary_router = APIRouter()


@notary_router.get("/", response_model=list[NotarySchema])
async def notary():
    return await Notary.all()
