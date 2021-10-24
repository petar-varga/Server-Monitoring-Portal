from fastapi import APIRouter

from api.routes import mysql_checks

api_router = APIRouter()
api_router.include_router(mysql_checks.router, tags=["Generic MYSQL Checks"])