from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.user import User


class UserRepository:

    def __init__(self, db: Session):
        self.db = db

    def find_by_username(self, username: str):
        statement = select(User).where(User.username == username)
        return self.db.scalar(statement)

    def create(self, user: User):
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)

        return user