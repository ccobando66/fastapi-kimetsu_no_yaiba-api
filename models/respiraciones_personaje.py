from sqlalchemy import(
    Integer,String,Column,
    ForeignKey
  
)

from config.config import Base

class RespiracionesPersonaje(Base):
    __tablename__ = 'respiraciones_personaje'
    id = Column(Integer, 
                     primary_key=True,
                     index=True,
                     autoincrement=True
    )
    id_personaje = Column(String,
                          ForeignKey('personaje.id_personaje')
    )
    id_respiracion = Column(
        String,
        ForeignKey('respiraciones.id')  
    )
