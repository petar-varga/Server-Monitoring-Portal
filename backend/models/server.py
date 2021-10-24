from sqlalchemy import Column, BigInteger, DateTime, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from db.base_class import Base

class Server(Base):
    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True, nullable=False)
    name = Column(Text, nullable=True, default=None)
    operating_system = Column(Text, nullable=True, default=None)
    ip = Column(Text, nullable=True, default=None)
    status = Column(Text, nullable=True, default="Initializing")
    date_added = Column(DateTime, nullable=True, default=func.now())
    date_updated = Column(DateTime, nullable=True, onupdate=func.now())
    