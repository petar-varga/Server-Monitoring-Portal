from fastapi import APIRouter

from api.routes import mysql_interface

api_router = APIRouter()
api_router.include_router(mysql_interface.router, tags=["Generic MYSQL Interface"])