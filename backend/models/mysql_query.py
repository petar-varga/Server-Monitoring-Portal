from sqlalchemy import Column, BigInteger, DateTime, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy.sql.schema import ForeignKey

from db.base_class import Base

class MySQLQuery(Base):
    __tablename__ = "mysql_query"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True, nullable=False)
    name = Column(Text, nullable=True, default=None)
    sql_query = Column(Text, nullable=True, default=None)
    date_added = Column(DateTime, nullable=True, default=func.now())
    date_updated = Column(DateTime, nullable=True, onupdate=func.now())
    account_id = Column(BigInteger, ForeignKey("account.id"), nullable=False)

    servers = relationship("MySQLQueryServerAssigned", back_populates="queries")
    owner_account = relationship("Account", back_populates="mysql_queries")
    