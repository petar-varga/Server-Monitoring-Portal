from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from crud.base import CRUDBase
from models.mysql_query import MySQLQuery
from schemas.mysql_query import MySQLQueryCreate, MySQLQueryCreateAccountOwner, MySQLQueryUpdate


class CRUDMySQLQuery(CRUDBase[MySQLQuery, MySQLQueryCreate, MySQLQueryUpdate]):
    def get_for_account_owner(
        self, db: Session, owner_id: int, id: int
    ) -> MySQLQuery:
        return db.query(self.model).filter(
            self.model.id == id,
            self.model.account_id == owner_id
        ).first()

    def create_for_account_owner(
        self, db: Session, *, 
        obj_in: MySQLQueryCreateAccountOwner
    ) -> MySQLQuery:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)  # type: ignore
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

mysql_query = CRUDMySQLQuery(MySQLQuery)