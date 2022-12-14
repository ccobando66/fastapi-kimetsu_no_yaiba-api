import uuid

from models import (
    espada,personaje,espada_personaje,
    respiraciones,respiraciones_personaje,tecnica,
    especie,especie_personaje,
    afiliacion,afiliacion_personaje,usuario
    
)

from schema import(
    personaje_schema
)

from fastapi import(
    APIRouter,status,HTTPException,
    Body,Path,Depends
)

from config.config import (
    conexion, Base,Seccion
)

from auth.Oauth2 import(
    oauth2_scheme
)

Base.metadata.create_all(conexion)
seccion = Seccion()


personajes = APIRouter()



@personajes.get(
    path='/',
    tags=['Personajes'],
    status_code=status.HTTP_200_OK
    
)
async def get_all_personajes():
    query = seccion.query(personaje.Personaje).all()
    seccion.close()
    return query

@personajes.get(
    path='/api/v1/personaje/{id_personaje}',
    status_code=status.HTTP_200_OK,
    tags=['Personajes']
)
async def get_personaje(
    id_personaje:str = Path(...)
):
    personaje_reciver = seccion.query(personaje.Personaje).get(id_personaje)
    
    if personaje_reciver is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Personaje no esta registrado")
    seccion.close()
    return personaje_reciver




@personajes.post(
    path='/api/v1/personaje',
    status_code=status.HTTP_201_CREATED,
    response_model=personaje_schema.Personaje,
    tags=['Personajes']
    )
async def create_personaje(
    personajes:personaje_schema.Personaje = Body(...)
):  
    personajes.id_personaje = str(uuid.uuid4())
    personaje_reciver = personaje.Personaje(
        id_personaje = personajes.id_personaje,
        nombre = personajes.nombre.strip(),
        apellido = personajes.apellido.strip(),
        edad = personajes.edad,
        resistencia = personajes.resistencia,
        poder = personajes.poder
    )
    seccion.add(personaje_reciver)
    seccion.commit()
    seccion.close()
    
    return personajes


@personajes.put(
    path='/api/v1/personaje/{id_personaje}',
    status_code=status.HTTP_200_OK,
    response_model=personaje_schema.Personaje,
    tags=['Personajes']
)
async def update_personaje(
    id_personaje:str = Path(...),
    personajes_body:personaje_schema.Personaje = Body(...)
):
    personaje_reciver = seccion.query(personaje.Personaje).get(id_personaje)
    
    if personaje_reciver is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Personaje no esta registrado")
    
    personaje_reciver.edad = personajes_body.edad
    personaje_reciver.resistencia = personajes_body.resistencia
    personaje_reciver.poder = personajes_body.poder
    
    personajes_body.id_personaje = personaje_reciver.id_personaje
    personajes_body.nombre = personaje_reciver.nombre
    personajes_body.apellido = personaje_reciver.apellido
    
    seccion.add(personaje_reciver)
    seccion.commit()
    seccion.close()
    
    return personajes_body

