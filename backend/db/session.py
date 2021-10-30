from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from core.config import settings

engine = create_engine(
    settings.SQLALCHEMY_DATABASE_URI,
    pool_size=100,
    max_overflow=50
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)