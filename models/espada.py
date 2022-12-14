from sqlalchemy import(
    String,Float,Column
)
from sqlalchemy.orm import relationship
from config.config import Base

class Espada(Base):
    __tablename__='espada'
    id_espada = Column(String,
                       primary_key=True,
                       nullable=False,
                       index=True
    )
    color = Column(String,
                   nullable=False
    )
    danio = Column(Float)
    vida = Column(Float,
                 server_default="100.0"   
    )
    
    personajes = relationship(
        'Personaje',
         secondary='espada_personaje',
         back_populates='espadas'   
    )
    
  
    