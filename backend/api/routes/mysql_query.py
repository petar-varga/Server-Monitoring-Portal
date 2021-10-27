from typing import List
import requests
import json

import crud
import models

from schemas.mysql_query import MySQLQueryCreateAccountOwner, MySQLQueryCreate, MySQLQuery, MySQLQueryList

from schemas.user import UserInDB

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

# importing custom dependencies
from api.deps import pwd_context, oauth2_scheme, basic_auth
from api.deps import get_current_active_user, get_db

from core.config import settings
import time

router = APIRouter()

@router.get("/get-sql-query-details", response_model=MySQLQuery)
async def get_sql_query_details(
        mysql_query_id: int,
        current_user: UserInDB = Depends(get_current_active_user),
        db: Session = Depends(get_db),
    ):
    current_user_fresh = crud.user.get(db, id=current_user.id)

    account_info = crud.mysql_query.get_single_for_account_owner(
        db, owner_id=current_user_fresh.account_id,
        id=mysql_query_id
    )

    return account_info

@router.get("/list", response_model=List[MySQLQueryList])
async def list_mysql_queries(
        current_user: UserInDB = Depends(get_current_active_user),
        db: Session = Depends(get_db),
    ):
    mysql_queries = crud.mysql_query.get_all_for_account_owner(db, current_user.account_id)

    return mysql_queries

@router.post("/add", response_model=MySQLQuery)
async def add_mysql_query(
        addition_data: MySQLQueryCreate,
        current_user: UserInDB = Depends(get_current_active_user),
        db: Session = Depends(get_db)
    ):
    account_id=crud.user.get(db, id=current_user.id).account_id
    addition_data = MySQLQueryCreateAccountOwner(
        **addition_data.dict(), 
        account_id=account_id
    )
    mysql_query = crud.mysql_query.create_for_account_owner(
        db=db, obj_in=addition_data
    )

    return mysql_query