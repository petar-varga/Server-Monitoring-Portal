from typing import List
import requests
import json

import crud
import models

from schemas.user import UserInDB
from schemas.server import ServerCreate, ServerListDetailsNoAccessToken, ServerListDetailsWithAccessToken

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

# importing custom dependencies
from api.deps import pwd_context, oauth2_scheme, basic_auth
from api.deps import get_current_active_user, get_db

from core.config import settings
import time

router = APIRouter()

def get_vltr_instances():
    url = "https://api.vultr.com/v2/instances"

    payload={}
    headers = {
        'Authorization': f'Bearer {settings.V_API_KEY}'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    json_object = json.loads(response.text)

    return json_object

@router.get("/single-server", response_model=ServerListDetailsNoAccessToken)
async def list_single_server_instance(
        server_id: int,
        current_user: UserInDB = Depends(get_current_active_user),
        db: Session = Depends(get_db),
    ):
    server = crud.server.get_single_for_account_owner(
        db, current_user.account_id, server_id
    )

    return server

@router.get("/list", response_model=List[ServerListDetailsNoAccessToken])
async def list_server_instances(
        current_user: UserInDB = Depends(get_current_active_user),
        db: Session = Depends(get_db),
    ):
    server_list = crud.server.get_for_account_owner(db, current_user.account_id)

    return server_list

@router.post("/add", response_model=ServerListDetailsWithAccessToken)
async def add_server_instance(
        addition_data: ServerCreate,
        current_user: UserInDB = Depends(get_current_active_user),
        db: Session = Depends(get_db)
    ):
    addition_data.owner_account_id = current_user.account_id
    server = crud.server.create(
        db=db, obj_in=addition_data
    )

    return server