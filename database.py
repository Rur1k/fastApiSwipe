import os

from dotenv import load_dotenv

load_dotenv()

TORTOISE_ORM = {
    "connections": {
         "default": os.getenv("DATABASE_URL")
    },
    "apps": {
        "users": {
            "models": [
                 "models", "aerich.models"
            ],
            "default_connection": "default",
        },
    },
}