from typing import List
import requests
import json

import crud
import models
from models.mysql_query_server_assignment import MySQLQueryServerAssignment

from schemas.mysql_query import MySQLQueryCreateAccountOwner, MySQLQueryCreate, MySQLQuery, MySQLQueryList
from schemas.mysql_query_server_assignment import MySQLQueryServerAllData, MySQLQueryServerAssignmentCreation

from schemas.user import UserInDB

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

# importing custom dependencies
from api.deps import pwd_context, oauth2_scheme, basic_auth
from api.deps import get_current_active_user, get_db

from core.config import settings
import time

router = APIRouter()

# @router.get("/get-sql-query-details", response_model=MySQLQuery)
# async def get_sql_query_details(
#         mysql_query_id: int,
#         current_user: UserInDB = Depends(get_current_active_user),
#         db: Session = Depends(get_db),
#     ):

#     account_info = crud.mysql_query.get_single_for_account_owner(
#         db, owner_id=current_user.account_id,
#         id=mysql_query_id
#     )

#     return account_info

@router.get("/list", response_model=List[MySQLQueryServerAllData])
async def list_mysql_queries_for_server(
        server_id: int,
        current_user: UserInDB = Depends(get_current_active_user),
        db: Session = Depends(get_db),
    ):
    mysql_queries = crud.server.get_single_for_account_owner(
        db, current_user.account_id, server_id
    ).queries

    return mysql_queries

@router.post("/add", response_model=MySQLQueryServerAssignmentCreation)
async def add_mysql_query_to_server(
        addition_data: MySQLQueryServerAssignmentCreation,
        current_user: UserInDB = Depends(get_current_active_user),
        db: Session = Depends(get_db)
    ):
    server = crud.server.get_single_for_account_owner(
        db, current_user.account_id, id=addition_data.server_id
    )
    assignment = MySQLQueryServerAssignment(**addition_data.dict())
    assignment.queries = crud.mysql_query.get_single_for_account_owner(
        db, current_user.account_id, id=addition_data.mysql_query_id
    )
    server.queries.append(assignment)

    db.add(server)
    db.commit()
    db.refresh(assignment)

    return assignment