from core.security import authenticate_user, create_access_token
from schemas.token import Token

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from starlette.responses import Response
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

# support for usage with Docs Authorize "flow"
@router.post("/token", response_model=Token)
async def route_login_access_token(response: Response, form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
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
