from typing import List
import requests
import json

import crud

from schemas.user import UserInDB
from schemas.server import ServerCreate, ServerListDetails

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

@router.get("/list", response_model=List[ServerListDetails])
async def list_vultr_instances(
        current_user: UserInDB = Depends(get_current_active_user),
        db: Session = Depends(get_db),
    ):
    server_list = crud.server.get_multi(db)

    return server_list

@router.post("/add", response_model=ServerListDetails)
async def list_vultr_instances(
        addition_data: ServerCreate,
        current_user: UserInDB = Depends(get_current_active_user),
        db: Session = Depends(get_db)
    ):
    time.sleep(2)
    server = crud.server.create(
        db=db, obj_in=addition_data
    )

    return server