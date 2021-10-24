from typing import List
import requests
import json

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core.config import settings
import time

router = APIRouter()

def perform_raw_sql_query():
    json_object = {
        "field_name": "field value"
    }

    return json_object

@router.get("/execute-generic-mysql-query", response_model=dict)
async def execute_generic_mysql_query(
        access_token: str
    ):

    result = perform_raw_sql_query()

    return result