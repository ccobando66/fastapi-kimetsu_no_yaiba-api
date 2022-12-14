from sqlalchemy import(
    Integer,String,Column,
    ForeignKey,Boolean
  
)

from config.config import Base

class EspeciePersonaje(Base):
    __tablename__ = 'especie_personaje'
    id = Column(Integer, 
                     primary_key=True,
                     index=True,
                     autoincrement=True
    )
    id_personaje = Column(String,
                          ForeignKey('personaje.id_personaje')
    )
    id_especie = Column(
        Integer,
        ForeignKey('especie.id')  
    )
    activo = Column(
        Boolean,
        server_default="true"   
    )