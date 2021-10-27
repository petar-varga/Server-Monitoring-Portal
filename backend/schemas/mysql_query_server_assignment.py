from os import access
from pydantic import BaseModel
from datetime import datetime

class MySQLQueryServerAssignmentBase(BaseModel):
    server_id: int
    mysql_query_id: int

    class Config:
        orm_mode = True

class MySQLQueryServerAssignmentCreation(MySQLQueryServerAssignmentBase):
    name: str
    notes: str

class MySQLQueryServerLastResult(MySQLQueryServerAssignmentCreation):
    query_result: str = None

class MySQLQueryServerAllData(MySQLQueryServerLastResult):
    date_added: datetime = None
    date_updated: datetime = None

    class Config:
        orm_mode = True