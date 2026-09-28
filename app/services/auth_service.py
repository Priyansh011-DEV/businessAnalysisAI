import bcrypt

from app.core.jwt import create_access_token
from app.models.user import User
from app.repositories.user_repository import UserRepository


class AuthService:

    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def register(self, username: str, password: str, tenant_id: int):
        existing_user = self.user_repository.find_by_username(username)

        if existing_user:
            raise ValueError("Username already exists")

        password_hash = bcrypt.hashpw(
            password.encode("utf-8"),
            bcrypt.gensalt()
        ).decode("utf-8")

        user = User(
            username=username,
            password_hash=password_hash,
            tenant_id=tenant_id,
            role="USER"
        )

        return self.user_repository.create(user)

    def login(self, username: str, password: str):
        user = self.user_repository.find_by_username(username)

        if not user:
            raise ValueError("Invalid username or password")

        password_valid = bcrypt.checkpw(
            password.encode("utf-8"),
            user.password_hash.encode("utf-8")
        )

        if not password_valid:
            raise ValueError("Invalid username or password")

        access_token = create_access_token(
            user_id=user.id,
            username=user.username,
            tenant_id=user.tenant_id,
            role=user.role
        )

        return access_token