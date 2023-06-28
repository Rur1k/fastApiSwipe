import os

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from tortoise.contrib.fastapi import register_tortoise
from tortoise.contrib.pydantic import pydantic_model_creator
from passlib.context import CryptContext
from email_validator import validate_email, EmailNotValidError

from models import User
from schemas import UserCreate

load_dotenv()

app = FastAPI()
user_pydantic = pydantic_model_creator(User)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@app.post("/user/register/", status_code=201)
async def register_user(user: UserCreate):
    if user.password != user.repeat_password:
        raise HTTPException(status_code=403, detail="Password mismatch")

    try:
        validate_email(user.email)
        hashed_password = pwd_context.hash(user.password)

        user = await User.create(email=user.email, hashed_password=hashed_password)
        return await user_pydantic.from_tortoise_orm(user)
    except EmailNotValidError as e:
        raise HTTPException(status_code=403, detail="Invalid email address")




register_tortoise(
    app,
    db_url=os.getenv("DATABASE_URL"),
    modules={"models": ["models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)
