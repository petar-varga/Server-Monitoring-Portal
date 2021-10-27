from typing import List
import json
import requests

import crud
from schemas.server_management import ExecuteMysqlQueryResponse

from schemas.user import UserInDB
from schemas.server import ServerCreate

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

# importing custom dependencies
from api.deps import pwd_context, oauth2_scheme, basic_auth
from api.deps import get_current_active_user, get_db

from core.config import settings
import time

router = APIRouter()

def get_api_response(server_ip, access_token, mysql_query):
    url = server_ip + f"?access_token={access_token}&query={mysql_query}"

    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    return response

@router.post("/get-and-wait-sql-query-result", response_model=ExecuteMysqlQueryResponse)
async def get_and_wait_sql_query_result(
        server_id: int,
        mysql_query_id: int,
        current_user: UserInDB = Depends(get_current_active_user),
        db: Session = Depends(get_db)
    ):

    current_user_fresh = crud.user.get(db, id=current_user.id)

    # get server info
    server = crud.server.get_single_for_account_owner(
        db, owner_id=current_user_fresh.account_id, 
        id=server_id)
    # get mysql query
    mysql_query = crud.mysql_query.get_single_for_account_owner(
        db, owner_id=current_user_fresh.account_id,
        id=mysql_query_id
    )
    start_time = time.time()
    # http://127.0.0.1:8500/api/v1/execute-generic-mysql-query
    response = get_api_response(f"{server.webserver_ip}/execute-generic-mysql-query", server.access_token, mysql_query.sql_query)

    end_time = time.time()
    
    try:
        json_response = json.loads(response.text)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail={'error': 'Bad target server response!'})

    if not isinstance(json_response, list):
        potential_error_response = json_response.get("detail", {}).get("error", None)
        if potential_error_response != None:
            raise HTTPException(403, detail={
                "error": "unauthorized response returned from target server"
            })
        
        raise HTTPException(403, detail={
            "error": "Unknown target server error"
        })

    return ExecuteMysqlQueryResponse(
        query_response = json_response,
        query_time_ms = (end_time - start_time) * 1000
    )