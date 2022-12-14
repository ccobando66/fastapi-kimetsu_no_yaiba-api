from sqlalchemy import(
    String, Boolean, Integer,Column,DateTime
) 

from config.config import Base

class Ususario(Base):
    __tablename__ = 'usuario'
    id = Column(
        Integer,
        primary_key=True,
        index=True,
        autoincrement=True
    )
    username = Column(
        String,
        unique=True,
        nullable=False
    )
    email = Column(
        String,
        unique=True,
        nullable=False
    )
    passwd = Column(
        String,
        nullable=False
    )
    disable = Column(
        Boolean,
        nullable=True
    )
    token = Column(
        String,
        nullable=False
    )
    expiration = Column(
        DateTime,
        nullable=False
    )