from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from crud.base import CRUDBase
from models.server import Server
from schemas.server import ServerCreate, ServerUpdate


class CRUDServer(CRUDBase[Server, ServerCreate, ServerUpdate]):
    def create_with_owner(
        self, db: Session, *, obj_in: ServerCreate, owner_id: int
    ) -> Server:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, owner_id=owner_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj
    
    def get_for_account_owner(
        self, db: Session, owner_id: int
    ) -> List[Server]:
        return db.query(self.model).filter(
            self.model.owner_account_id == owner_id
        ).all()

server = CRUDServer(Server)