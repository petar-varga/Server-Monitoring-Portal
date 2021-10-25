from typing import Generator

from fastapi import HTTPException
from starlette.status import HTTP_403_FORBIDDEN

from db.session import SessionLocal

from core.config import settings

def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

def verify_access_token(access_token: str) -> bool:
    if access_token != settings.PRIVATE_ACCESS_TOKEN:
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN, detail={
                "error": "unauthorized"
            }
        )
    return access_token