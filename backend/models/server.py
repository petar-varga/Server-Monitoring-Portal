from typing import TYPE_CHECKING
from sqlalchemy import Column, BigInteger, DateTime, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Integer

from db.base_class import Base

if TYPE_CHECKING:
    # from .user import User  # noqa: F401
    from models.account import Account

class Server(Base):
    __tablename__ = "server"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True, nullable=False)
    name = Column(Text, nullable=True, default=None)
    operating_system = Column(Text, nullable=True, default=None)
    ip = Column(Text, nullable=True, default=None)
    status = Column(Text, nullable=True, default="Initializing")
    access_token = Column(Text, nullable=True, default=None)
    webserver_ip = Column(Text, nullable=True, default=None)
    date_added = Column(DateTime, nullable=True, default=func.now())
    date_updated = Column(DateTime, nullable=True, onupdate=func.now())
    owner_account_id = Column(BigInteger, ForeignKey("account.id"))
    
    queries = relationship("MySQLQueryServerAssignment", back_populates="servers")
    owner = relationship("Account", back_populates="servers")
    