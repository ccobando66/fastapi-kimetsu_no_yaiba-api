from models import (
    espada,espada_personaje
   
)

from config.config import (
    conexion, Base,Seccion
)

Base.metadata.create_all(conexion)
seccion = Seccion()

def helpers_get_espadas_personajes(value:str) -> list:
    query = (seccion.query(espada.Espada.id_espada,
                           espada.Espada.color,
                           espada.Espada.danio.label('daño_recibido'),
                           espada.Espada.vida
    ).join(espada_personaje.EspadaPersonaje, espada_personaje.EspadaPersonaje.id_espada == espada.Espada.id_espada)
     .filter(espada_personaje.EspadaPersonaje.id_personaje == value.strip())
    ).all()
    return query