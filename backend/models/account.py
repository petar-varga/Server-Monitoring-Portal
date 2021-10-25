from sqlalchemy import Column, BigInteger, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy.sql.sqltypes import Boolean, DateTime

from db.base_class import Base

class Account(Base):
    __tablename__ = "account"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True, nullable=False)
    name = Column(Text, nullable=False)
    date_added = Column(DateTime, nullable=True, default=func.now())
    date_updated = Column(DateTime, nullable=True, onupdate=func.now())

    users = relationship("User", back_populates="account_group")
    servers = relationship("Server", back_populates="owner")
    mysql_queries = relationship("MySQLQuery", back_populates="owner_account")
    