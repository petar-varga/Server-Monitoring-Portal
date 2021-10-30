from typing import List
import requests
import json

import sqlalchemy

import crud
import models
from models.mysql_query_server_assignment import MySQLQueryServerAssignment
from schemas.generic import GenericResponse

from schemas.mysql_query import MySQLQueryCreateAccountOwner, MySQLQueryCreate, MySQLQuery, MySQLQueryList
from schemas.mysql_query_server_assignment import MySQLQueryServerAllData, MySQLQueryServerAssignmentBase, MySQLQueryServerAssignmentCreation, MySQLQueryServerExecuteQuery, MySQLQueryServerNoConnectionInfo

from schemas.user import UserInDB

from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks
from sqlalchemy.orm import Session

# importing custom dependencies
from api.deps import pwd_context, oauth2_scheme, basic_auth
from api.deps import get_current_active_user, get_db

from core.config import settings
from db.session import SessionLocal

import time

router = APIRouter()

def get_api_response(
        matched_sql_query: MySQLQueryServerAssignment, 
        webserver_ip, access_token, mysql_query
    ):
    url = webserver_ip + f"/execute-generic-mysql-query?access_token={access_token}&query={mysql_query}"

    response = requests.request("GET", url)
    
    # because of https://stackoverflow.com/questions/24291933/sqlalchemy-object-already-attached-to-session
    db: Session = SessionLocal()
    matched_sql_query = db.merge(matched_sql_query)
    matched_sql_query.query_result = response.text

    db.add(matched_sql_query)
    db.commit()
    db.refresh(matched_sql_query)

    return response

@router.post("/execute-assigned-no-wait", response_model=GenericResponse)
async def execute_assigned_background(
        execution_info: MySQLQueryServerExecuteQuery,
        background_tasks: BackgroundTasks,
        current_user: UserInDB = Depends(get_current_active_user),
        db: Session = Depends(get_db),
    ):
    matched_server = crud.server.get_single_for_account_owner(
        db, current_user.account_id, execution_info.server_id
    )

    if matched_server is None:
        raise HTTPException(401, detail={
            "error": "You don't have the rights to perform actions on this server"
        })

    matched_sql_query = None
    mysql_queries: List[MySQLQueryServerAssignment] = matched_server.queries
    for query in mysql_queries:
        if query.mysql_query_id == execution_info.mysql_query_id:
            matched_sql_query = query
            break
    
    if matched_sql_query is None:
        raise HTTPException(401, detail={
            "error": "You don't have the rights to perform the mysql query"
        })
    
    if matched_server.webserver_ip == None or matched_server.access_token == None:
        raise HTTPException(500, detail={
            "error": "Server doesn't have access token and web server IP configured"
        })

    query_info: models.MySQLQuery = matched_sql_query.queries

    matched_sql_query: MySQLQueryServerAssignment = matched_sql_query # type hinting reason
    
    background_tasks.add_task(
        get_api_response,
        matched_sql_query=matched_sql_query,
        webserver_ip=matched_server.webserver_ip,
        access_token=matched_server.access_token,
        mysql_query=query_info.sql_query
    )

    return GenericResponse(
        status="OK", 
        status_display="Query is scheduled to be executed, please wait!"
    )

@router.get("/list", response_model=List[MySQLQueryServerNoConnectionInfo])
async def list_mysql_queries_for_server(
        server_id: int,
        current_user: UserInDB = Depends(get_current_active_user),
        db: Session = Depends(get_db),
    ):
    mysql_queries = crud.server.get_single_for_account_owner(
        db, current_user.account_id, server_id
    ).queries

    return mysql_queries

@router.post("/add", response_model=MySQLQueryServerAssignmentBase)
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

    try:
        db.commit()
    except sqlalchemy.exc.IntegrityError:
        raise HTTPException(500, detail={
            "error": "Duplicate MySQL Query assignments for same server are not allowed!"
        })

    db.refresh(assignment)
    return assignment