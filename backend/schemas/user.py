from pydantic import BaseModel

class UserBase(BaseModel):
    email: str

class User(UserBase):
    first_name: str
    last_name: str

class UserInDB(User):
    hashed_password: str
    disabled: bool = None

    class Config:
        orm_mode = True