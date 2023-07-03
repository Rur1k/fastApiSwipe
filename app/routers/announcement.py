from fastapi import APIRouter
from fastapi import Depends, HTTPException, status
from config.settings import get_settings
from models.users import Announcement

from schemas.announcement import AnnouncementSchema

settings = get_settings()
announcement_router = APIRouter()


@announcement_router.get("/", response_model=list[AnnouncementSchema])
async def announcements():
    return await Announcement.all()
