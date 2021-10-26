import secrets
from typing import Any, Dict, List, Optional, Union

from pydantic import AnyHttpUrl, BaseSettings, EmailStr, HttpUrl, validator

from core.secret_data_loading import MYSQL_DATABASE_ENV, MYSQL_PASSWORD_ENV, MYSQL_SERVER_ENV, MYSQL_USERNAME_ENV, API_KEY

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = "somesecretkey123029" #secrets.token_urlsafe(32)
    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    ALGORITHM: str = "HS256"

    SERVER_NAME: str = "Dev_SERVER"
    SERVER_HOST: AnyHttpUrl = "http://localhost"
    # BACKEND_CORS_ORIGINS is a JSON-formatted list of origins
    # e.g: '["http://localhost", "http://localhost:4200", "http://localhost:3000", \
    # "http://localhost:8080", "http://local.dockertoolbox.tiangolo.com"]'
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = [
        "http://localhost", "http://localhost:4200", 
        "http://localhost:3000", "http://localhost:8080"
    ]

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    PROJECT_NAME: str = "DEV Test Project"

    MYSQL_SERVER: str = MYSQL_SERVER_ENV
    MYSQL_USER: str = MYSQL_USERNAME_ENV
    MYSQL_PASSWORD: str = MYSQL_PASSWORD_ENV
    MYSQL_DB: str = MYSQL_DATABASE_ENV
    V_API_KEY: str = API_KEY
    SQLALCHEMY_DATABASE_URI: str = None

    # this auto builds the sqlalchemy database uri
    @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> str:
        if not v:
            # TODO: HARDCODE FIX, UNCOMMENT TO USE ACTUAL VALUES
            return f'mysql://root:@localhost:3307/server_management_portal'
            return f'mysql://{values["MYSQL_USER"]}:{values["MYSQL_PASSWORD"]}@{values["MYSQL_SERVER"]}/{values["MYSQL_DB"]}'
        return v

    class Config:
        case_sensitive = True


settings = Settings()