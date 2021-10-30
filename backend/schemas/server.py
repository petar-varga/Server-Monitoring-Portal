from os import access
from pydantic import BaseModel

class ServerBase(BaseModel):
    name: str

# Properties to receive on server creation
class ServerCreate(ServerBase):
    ip: str
    # can be supplied - will be overriden to actual 
    # account owner for user that creates it
    owner_account_id: str = None

# Properties to receive on server update
class ServerUpdate(ServerBase):
    id: int
    ip: str

class ServerListDetailsNoAccessToken(ServerBase):
    id: int
    ip: str
    webserver_ip: str = None
    operating_system: str = None
    status: str = None

    class Config:
        orm_mode = True

class ServerListDetailsWithAccessToken(ServerListDetailsNoAccessToken):
    access_token: str = None
