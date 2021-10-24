from pydantic import BaseModel

class ServerBase(BaseModel):
    name: str

# Properties to receive on server creation
class ServerCreate(ServerBase):
    ip: str

# Properties to receive on server update
class ServerUpdate(ServerBase):
    id: int
    ip: str

class ServerListDetails(ServerBase):
    id: int
    ip: str
    operating_system: str = None
    status: str = None

    class Config:
        orm_mode = True
