from sqlalchemy import(
    Integer,String,Column,
    ForeignKey
)
from sqlalchemy.orm import relationship
from config.config import Base

class Naturaleza(Base):
    __tablename__ = 'naturaleza'
    id = Column(Integer, 
                     primary_key=True,
                     index=True,
                     autoincrement=True
    )
    nombre = Column(String,
                    nullable=False
    )
    principal = Column(
        String,
        server_default="Solar"
        
    )
    
    

class Respiraciones(Base):
    __tablename__ = 'respiraciones'
    id = Column(String, 
                     primary_key=True,
                     index=True
    )
    nombre = Column(
        String,
        nullable=False
    )
    id_naturaleza = Column(Integer,
                    ForeignKey('naturaleza.id')
    )
    naturalezas = relationship('Naturaleza', cascade='all, delete')
    
    personajes = relationship(
        'Personaje',
         secondary='respiraciones_personaje',
         back_populates='respiraciones'
    )
    
    