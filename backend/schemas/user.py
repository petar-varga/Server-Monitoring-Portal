from pydantic import BaseModel

class UserBase(BaseModel):
    email: str

class User(UserBase):
    first_name: str
    last_name: str

# Properties to receive on user creation
class UserCreate(User):
    password: str
    disabled: bool = False
    account_id: int

# Properties to receive on user update
class UserUpdate(User):
    id: int

class UserInDB(User):
    id: int
    account_id: int
    hashed_password: str
    disabled: bool = None

    class Config:
        orm_mode = True