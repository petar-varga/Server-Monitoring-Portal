from pydantic import BaseModel
from datetime import datetime

class AccountBase(BaseModel):
    name: str

# Properties to receive on server creation
class AccountCreate(AccountBase):
    pass

# Properties to receive on server update
class AccountUpdate(AccountBase):
    pass

class AccountDetails(AccountBase):
    date_added: datetime = None
    date_updated: datetime = None

    class Config:
        orm_mode = True