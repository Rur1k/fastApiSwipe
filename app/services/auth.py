from config.settings import get_settings
from passlib.context import CryptContext

settings = get_settings()


class Auth:
    password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    @classmethod
    def get_password_hash(cls, password: str) -> str:
        return cls.password_context.hash(password)

    @classmethod
    def verify(cls, hash_password: str, password: str) -> bool:
        return cls.password_context.verify(password, hash_password)
