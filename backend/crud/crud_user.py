from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from crud.base import CRUDBase
from models.user import User
from schemas.user import UserCreate, UserUpdate

class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):
    def get_by_email(
        self, db: Session, email: str
    ) -> User:
        return db.query(self.model).filter(
            self.model.email == email
        ).first()

user = CRUDUser(User)