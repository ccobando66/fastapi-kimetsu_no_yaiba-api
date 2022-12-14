from sqlalchemy import(
    Integer,String,Column,
    ForeignKey
  
)

from config.config import Base

class EspadaPersonaje(Base):
    __tablename__ = 'espada_personaje'
    id = Column(Integer, 
                     primary_key=True,
                     index=True,
                     autoincrement=True
    )
    id_personaje = Column(String,
                          ForeignKey('personaje.id_personaje')
    )
    id_espada = Column(
        String,
        ForeignKey('espada.id_espada')  
    )
