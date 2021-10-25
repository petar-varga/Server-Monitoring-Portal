from typing import List
import requests
import json

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core.config import settings
import time

from api.deps import verify_access_token

router = APIRouter()

def perform_raw_sql_query():
    db_result = [
        {
            "field_name": "field value"
        }
    ]

    return db_result

@router.get("/execute-generic-mysql-query", response_model=List[dict])
async def execute_generic_mysql_query(
        access_token: str = Depends(verify_access_token)
    ):

    result = perform_raw_sql_query()

    return result