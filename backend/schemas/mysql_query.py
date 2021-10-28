from pydantic import BaseModel
from datetime import datetime

class MySQLQueryBase(BaseModel):
    name: str

class MySQLQuery(MySQLQueryBase):
    sql_query: str

    class Config:
        orm_mode = True

# Properties to receive on user creation
class MySQLQueryCreate(MySQLQuery):
    pass

# Properties to receive on user update
class MySQLQueryUpdate(MySQLQuery):
    id: int

class MySQLQueryList(MySQLQuery):
    id: int

    class Config:
        orm_mode = True

class MySQLQueryListAssigned(MySQLQuery):
    id: int
    is_assigned: bool

    class Config:
        orm_mode = True

class MySQLQueryCreateAccountOwner(MySQLQueryCreate):
    account_id: int

class MySQLQueryInDB(MySQLQuery):
    id: int
    account_id: int
    date_added: datetime
    date_created: datetime

    class Config:
        orm_mode = True