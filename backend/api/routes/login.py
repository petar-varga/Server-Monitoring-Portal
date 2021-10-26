from core.security import authenticate_user, create_access_token
from schemas.token import Token
from schemas.user import User, UserBase, UserInDB
import base64

from pydantic import BaseModel

from fastapi import APIRouter, Depends, FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.security import OAuth2PasswordRequestForm
from starlette.status import HTTP_403_FORBIDDEN
from starlette.responses import RedirectResponse, Response, JSONResponse
from starlette.requests import Request

# importing custom dependencies
from api.deps import pwd_context, oauth2_scheme, basic_auth
from api.deps import get_current_active_user

from core.cookie_auth_session import BasicAuth

from schemas.login import LoginCheck

router = APIRouter()

fake_users_db = {
    "johndoe@example.com": {
        "id": 1,
        "account_id": 2,
        "username": "johndoe",
        "full_name": "John Doe",
        "first_name": "John",
        "last_name": "Doe",
        "email": "johndoe@example.com",
        "hashed_password": "fakehashedsecret",
        "disabled": False,
    }
}

@router.post("/login", response_model=Token)
async def login_jwt(login_data: LoginCheck, response: Response):
    user = authenticate_user(fake_users_db, login_data.email, login_data.password)
    if not user:
        raise HTTPException(status_code=400, detail={'error': 'Incorrect email or password'})
    access_token = create_access_token(
        data={"sub": user.email}
    )
    response.set_cookie(
        "Authorization",
        value=f"Bearer {access_token}",
        httponly=True,
        max_age=1800,
        expires=1800,
    )
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/auth_user", response_model=UserBase)
async def auth_user_check(current_user: UserInDB = Depends(get_current_active_user)):
    return current_user

@router.get("/logout")
async def route_logout_and_remove_cookie():
    response = RedirectResponse(url="/")
    response.delete_cookie("Authorization")
    return response