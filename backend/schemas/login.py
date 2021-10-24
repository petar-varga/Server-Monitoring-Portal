from pydantic import BaseModel

class LoginBase(BaseModel):
    email: str

class LoginCheck(LoginBase):
    password: str
