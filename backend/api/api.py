from fastapi import APIRouter

from api.routes import login
from api.routes import server
from api.routes import server_management
from api.routes import mysql_query
from api.routes import account
from api.routes import mysql_query_server_assignment

api_router = APIRouter()
api_router.include_router(login.router, tags=["Login"])
api_router.include_router(server.router, prefix="/server", tags=["Servers"])
api_router.include_router(mysql_query.router, prefix="/mysql-query", tags=["MySQL Queries"])
api_router.include_router(mysql_query_server_assignment.router, prefix="/mysql-query-server", tags=["MySQL Query - Server assignment"])
api_router.include_router(server_management.router, prefix="/server-management", tags=["Server Management"])
api_router.include_router(account.router, prefix="/account", tags=["Accounts"])