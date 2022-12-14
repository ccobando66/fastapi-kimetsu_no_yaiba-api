from sqlalchemy import(
    String,Column,Float,
    ForeignKey
  
)
from config.config import Base

class Tecnica(Base):
    __tablename__ = 'tecnica'
    id = Column(String, 
                     primary_key=True,
                     index=True
    )
    nombre = Column(String,
                    nullable=False
    )
    danio = Column(Float)
    personaje = Column(String,
                       ForeignKey('personaje.id_personaje')
    )
    