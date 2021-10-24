from fastapi import APIRouter

from api.routes import login
from api.routes import vultr_integration

api_router = APIRouter()
api_router.include_router(login.router, tags=["Login"])
api_router.include_router(vultr_integration.router, prefix="/vultr-integration", tags=["Vultr Integration"])