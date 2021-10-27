from typing import List
import requests
import json

import crud
import models
from schemas.account import AccountCreate, AccountDetails

from schemas.user import UserInDB

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

# importing custom dependencies
from api.deps import pwd_context, oauth2_scheme, basic_auth
from api.deps import get_current_active_user, get_db

from core.config import settings
import time

router = APIRouter()

@router.get("/get_account_info", response_model=AccountDetails)
async def get_account_info(
        current_user: UserInDB = Depends(get_current_active_user),
        db: Session = Depends(get_db),
    ):
    account_info = crud.account.get(db, id = current_user.account_id)

    return account_info

@router.post("/add", response_model=AccountDetails)
async def add_account(
        addition_data: AccountCreate,
        db: Session = Depends(get_db)
    ):
    account = crud.account.create(
        db=db, obj_in=addition_data
    )

    return account