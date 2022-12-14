from sqlalchemy import(
    Integer,String,Column,Float,Boolean
  
)

from sqlalchemy.orm import relationship
from config.config import Base


class Especie(Base):
    __tablename__ = 'especie'
    id = Column(Integer, 
                     primary_key=True,
                     index=True,
                     autoincrement=True
    )
    nombre = Column(String,
                    nullable=False
    )
    vida = Column(
        Float,
        server_default="100.0"
    )
    
    
    personajes = relationship(
        'Personaje',
         secondary='especie_personaje',
         back_populates='especies'
    )
    
  

