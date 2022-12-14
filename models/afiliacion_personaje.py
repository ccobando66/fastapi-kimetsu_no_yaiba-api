from sqlalchemy import(
    Integer,String,Column,
    ForeignKey
  
)

from config.config import Base

class AfiliacionPersonaje(Base):
    __tablename__ = 'afiliacion_personaje'
    id = Column(Integer, 
                     primary_key=True,
                     index=True,
                     autoincrement=True
    )
    id_personaje = Column(String,
                          ForeignKey('personaje.id_personaje')
    )
    id_afiliacion = Column(
        Integer,
        ForeignKey('afiliacion.id_afiliacion')  
    )
