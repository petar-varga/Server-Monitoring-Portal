from fastapi import APIRouter

from api.routes import login
from api.routes import server
from api.routes import server_management

api_router = APIRouter()
api_router.include_router(server_management.router, prefix="/server-management", tags=["Server Management"])
api_router.include_router(login.router, tags=["Login"])
api_router.include_router(server.router, prefix="/server", tags=["Servers"])