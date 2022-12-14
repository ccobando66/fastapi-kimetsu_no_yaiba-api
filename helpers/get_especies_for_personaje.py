from models import (
    especie,especie_personaje
   
)

from config.config import (
    conexion, Base,Seccion
)

Base.metadata.create_all(conexion)
seccion = Seccion()

def helpers_get_especie_personajes(value:str) -> list:
    response =  (seccion.query(
                                especie.Especie.nombre.label('Raza'),
                                especie.Especie.vida,
                                especie_personaje.EspeciePersonaje.activo
                               )
                 .join(especie_personaje.EspeciePersonaje, especie_personaje.EspeciePersonaje.id_especie == especie.Especie.id)
                 .filter(especie_personaje.EspeciePersonaje.id_personaje == value.strip())
                 .filter(especie_personaje.EspeciePersonaje.activo == True)
                ).all()
    return response