from typing import TYPE_CHECKING
from sqlalchemy import Column, BigInteger, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Boolean, DateTime

from db.base_class import Base
if TYPE_CHECKING:
    # from .user import User  # noqa: F401
    from models.account import Account

class User(Base):
    __tablename__ = "user"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True, nullable=False)
    email = Column(Text, nullable=False)
    first_name = Column(Text, nullable=False)
    last_name = Column(Text, nullable=False)
    hashed_password = Column(Text, nullable=False)
    disabled = Column(Boolean, nullable=True, default=False)
    date_added = Column(DateTime, nullable=True, default=func.now())
    date_updated = Column(DateTime, nullable=True, onupdate=func.now())
    account_id = Column(BigInteger, ForeignKey("account.id"), nullable=False)

    account_group = relationship("Account", back_populates="users")