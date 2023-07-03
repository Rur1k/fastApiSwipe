from fastapi import APIRouter
from fastapi import Depends, HTTPException, status
from services.auth import Auth
from config.settings import get_settings
from models import users
from schemas.create_user import UserCreate
from schemas.login_user import UserLogin

settings = get_settings()
auth_router = APIRouter()


@auth_router.post("/register")
async def register(form_data: UserCreate = Depends()):
    if await users.User.get_or_none(email=form_data.email) is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User already exists."
        )

    if form_data.password == form_data.repeat_password:
        user = await users.User.create(
            email=form_data.email,
            hashed_password=Auth.get_password_hash(
                form_data.password.get_secret_value()
            )
        )
        await user.save()
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Password mismatch."
        )


@auth_router.post("/login")
async def register(form_data: UserLogin = Depends()):
    user = await users.User.get_or_none(email=form_data.email)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect username or password"
        )

    if Auth.verify(user.hashed_password, form_data.password):
        return {"access_token": "token", "token_type": "bearer"}

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Incorrect username or password"
    )

