from pydantic import BaseModel

class ServerInfo(BaseModel):
    name: str
    ip: str

class ServerInstance(BaseModel):
    id: int
    serverInfo: ServerInfo
    operatingSystem: str = None
    status: str = None