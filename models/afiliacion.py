from sqlalchemy import(
    Integer,String,Column,
    ForeignKey
)
from sqlalchemy.orm import relationship
from config.config import Base

class Tipo(Base):
    __tablename__ = 'tipo'
    id_tipo = Column(Integer, 
                     primary_key=True,
                     index=True,
                     autoincrement=True
    )
    nombre = Column(String,
                    nullable=False
    )
    
    

class Afiliacion(Base):
    __tablename__ = 'afiliacion'
    id_afiliacion = Column(Integer, 
                     primary_key=True,
                     index=True,
                     autoincrement=True
    )
    nombre = Column(
        String,
        nullable=False
    )
    tipos = Column(Integer,
                   ForeignKey('tipo.id_tipo')
    )
    rel_tipo = relationship('Tipo')
    
    personajes = relationship(
        'Personaje',
         secondary='afiliacion_personaje',
         back_populates='afiliaciones'
    )
   