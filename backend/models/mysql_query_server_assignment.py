from sqlalchemy import Column, BigInteger, DateTime, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy.sql.schema import ForeignKey

from db.base_class import Base

class MySQLQueryServerAssignment(Base):
    __tablename__ = 'mysql_query_server_assignment'

    server_id = Column(ForeignKey('server.id'), primary_key=True)
    mysql_query_id = Column(ForeignKey('mysql_query.id'), primary_key=True)

    date_added = Column(DateTime, nullable=True, default=func.now())
    date_updated = Column(DateTime, nullable=True, onupdate=func.now())
    query_result = Column(Text, nullable=True, default=None)

    queries = relationship("MySQLQuery", back_populates="servers")
    servers = relationship("Server", back_populates="queries")
