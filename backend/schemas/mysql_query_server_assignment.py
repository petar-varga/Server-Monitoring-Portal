from os import access
from pydantic import BaseModel
from datetime import datetime

class MySQLQueryServerAssignmentBase(BaseModel):
    name: str = None
    notes: str = None
    server_id: int
    mysql_query_id: int

    class Config:
        orm_mode = True

class MySQLQueryServerAssignmentCreation(MySQLQueryServerAssignmentBase):
    mysql_username: str
    mysql_password: str = ""
    mysql_host: str
    mysql_port: str = "3306"
    mysql_database: str
    
class MySQLQueryServerLastResult(MySQLQueryServerAssignmentCreation):
    query_result: str = None

class MySQLQueryServerAllData(MySQLQueryServerLastResult):
    date_added: datetime = None
    date_updated: datetime = None

    class Config:
        orm_mode = True