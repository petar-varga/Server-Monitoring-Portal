from typing import List
import requests
import json

import crud
import models
from models.mysql_query_server_assignment import MySQLQueryServerAssignment

from schemas.mysql_query import MySQLQueryCreateAccountOwner, MySQLQueryCreate, MySQLQuery, MySQLQueryList, MySQLQueryAssignedList

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

    account_info = crud.mysql_query.get_single_for_account_owner(
        db, owner_id=current_user.account_id,
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

@router.get("/list-server-assignment", response_model=List[MySQLQueryAssignedList])
async def list_mysql_queries_with_assignment(
        server_id: int,
        current_user: UserInDB = Depends(get_current_active_user),
        db: Session = Depends(get_db),
    ):
    assigned_mysql_queries: List[MySQLQueryServerAssignment] = crud.server.get_single_for_account_owner(
        db, current_user.account_id, server_id
    ).queries
    
    assigned_mysql_queries_ids = [x.mysql_query_id for x in assigned_mysql_queries]

    mysql_queries: List[MySQLQueryAssignedList] = crud.mysql_query.get_all_for_account_owner(db, current_user.account_id)
    for mysql_query in mysql_queries:
        if mysql_query.id in assigned_mysql_queries_ids:
            for assigned_query in assigned_mysql_queries:
                if assigned_query.mysql_query_id == mysql_query.id:
                    mysql_query.is_assigned = True
                    mysql_query.assignment_name = assigned_query.name
                    mysql_query.notes = assigned_query.notes
                    mysql_query.query_result = assigned_query.query_result
                    break
        else:
            mysql_query.is_assigned = False

    return mysql_queries

@router.post("/add", response_model=MySQLQuery)
async def add_mysql_query(
        addition_data: MySQLQueryCreate,
        current_user: UserInDB = Depends(get_current_active_user),
        db: Session = Depends(get_db)
    ):
    addition_data = MySQLQueryCreateAccountOwner(
        **addition_data.dict(), 
        account_id=current_user.account_id
    )
    mysql_query = crud.mysql_query.create_for_account_owner(
        db=db, obj_in=addition_data
    )

    return mysql_query