from core.security import authenticate_user, create_access_token
from schemas.token import Token
from sqlalchemy.orm import Session

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from starlette.responses import Response
from api.deps import get_db

router = APIRouter()


# support for usage with Docs Authorize "flow"
@router.post("/token", response_model=Token)
async def route_login_access_token(
    response: Response, form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    user = authenticate_user(db, form_data.username, form_data.password)
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
