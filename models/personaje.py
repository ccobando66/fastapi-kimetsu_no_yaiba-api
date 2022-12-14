from sqlalchemy import(
    Integer,String,Column,Float
  
)
from sqlalchemy.orm import relationship
from config.config import Base

class Personaje(Base):
    __tablename__ = 'personaje'
    id_personaje = Column(String, 
                     primary_key=True,
                     index=True
    )
    nombre = Column(String,
                    nullable=False
    )
    apellido = Column(String,
                      nullable=False
    )
    edad = Column(Integer,
                  nullable=False
    )
    resistencia = Column(
        Float
    )
    poder = Column(
        Float
    )
    
    tecnicas = relationship('Tecnica')
    
    espadas = relationship(
        'Espada',
         secondary='espada_personaje',
         back_populates='personajes'
    )
    
    respiraciones = relationship(
        'Respiraciones',
         secondary='respiraciones_personaje',
         back_populates='personajes',
         
    )
    
    afiliaciones = relationship(
        'Afiliacion',
         secondary='afiliacion_personaje',
         back_populates='personajes'
        
    )
    
    especies = relationship(
        'Especie',
         secondary='especie_personaje',
         back_populates='personajes'
         
    )
    
    