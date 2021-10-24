from pydantic import BaseModel

class UserBase(BaseModel):
    email: str = None
    username: str = None

class User(UserBase):
    full_name: str = None

class UserInDB(User):
    hashed_password: str
    disabled: bool = None