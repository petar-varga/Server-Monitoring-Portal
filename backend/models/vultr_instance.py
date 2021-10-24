from pydantic import BaseModel

class ServerInfo(BaseModel):
    name: str
    ip: str

class ServerInstance(BaseModel):
    id: str
    server_info: ServerInfo
    operating_system: str = None
    status: str = None