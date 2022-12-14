from models import (
    afiliacion,afiliacion_personaje
   
)

from config.config import (
    conexion, Base,Seccion
)

Base.metadata.create_all(conexion)
seccion = Seccion()

def helpers_get_afiliacion_personajes(value:str) -> list:
    query = (seccion.query(afiliacion.Afiliacion.nombre.label('Rango'),
                           afiliacion.Tipo.nombre.label('Afiliacion')
    ).join(afiliacion.Tipo, afiliacion.Tipo.id_tipo == afiliacion.Afiliacion.tipos)
     .join(afiliacion_personaje.AfiliacionPersonaje, afiliacion_personaje.AfiliacionPersonaje.id_afiliacion == afiliacion.Afiliacion.id_afiliacion)
     .filter(afiliacion_personaje.AfiliacionPersonaje.id_personaje == value.strip())
    ).all()
    return query