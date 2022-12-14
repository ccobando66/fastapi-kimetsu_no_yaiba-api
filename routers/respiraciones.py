from typing import List

import uuid

from models import (
    personaje,respiraciones,respiraciones_personaje
   
)

from auth.Oauth2 import(
   get_current_active_user
)

from schema import(
   respiraciones_schema,respiraciones_personaje_schema
)

from fastapi import(
    APIRouter,status,HTTPException,
    Body,Path,Depends
)

from config.config import (
    conexion, Base,Seccion
)

Base.metadata.create_all(conexion)
seccion = Seccion()

respiracion = APIRouter()

@respiracion.get(
    path='/api/v1/respiracion',
    status_code=status.HTTP_200_OK,
    tags=['Respiraciones']
)
async def get_all_respiraciones(token:str = Depends(get_current_active_user)):
    query = seccion.query(respiraciones.Respiraciones).all()
    return query


@respiracion.get(
    path='/api/v1/respiracion/{id_respiracion}',
    status_code=status.HTTP_200_OK,
    tags=['Respiraciones']
)
async def get_respiraciones(
    id_respiracion:str = Path(...),
    token:str = Depends(get_current_active_user)
):
    query = seccion.query(respiraciones.Respiraciones).get(id_respiracion.strip())
    if query is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='no existe la respiracion')
    return query

@respiracion.get(
    path='/api/v1/respiracion/personaje/{id_personaje}',
    status_code=status.HTTP_200_OK,
    tags=['Respiraciones']
)
async def get_respiraciones_personajes(
    id_personaje:str = Path(...),
    token:str = Depends(get_current_active_user)
):
    query = (seccion.query(
        respiraciones.Respiraciones.nombre,
        respiraciones.Naturaleza.nombre.label('Respiracion'),
        respiraciones.Naturaleza.principal,
    ).join(respiraciones.Respiraciones, respiraciones.Respiraciones.id_naturaleza == respiraciones.Naturaleza.id)
     .join(respiraciones_personaje.RespiracionesPersonaje,respiraciones_personaje.RespiracionesPersonaje.id_respiracion == respiraciones.Respiraciones.id)
     .filter(respiraciones_personaje.RespiracionesPersonaje.id_personaje == id_personaje.strip())
    ).all()
    return query


@respiracion.post(
    path='/api/v1/respiracion/',
    status_code=status.HTTP_200_OK,
    response_model=respiraciones_schema.Respiraciones,
    tags=['Respiraciones']
)
async def create_respiraciones(
    respiracion:respiraciones_schema.Respiraciones = Body(...),
    token:str = Depends(get_current_active_user)
):  
    respiracion.id = str(uuid.uuid4())
    
    respiracion_recived = respiraciones.Respiraciones(
        id = respiracion.id,
        nombre = respiracion.nombre.strip()
    )
    naturaleza = seccion.query(respiraciones.Naturaleza).get(respiracion.id_naturaleza)
    seccion.add(respiracion_recived)
    respiracion_recived.naturalezas = naturaleza
    seccion.commit()
    seccion.close()
    return respiracion

@respiracion.post(
    path='/api/v1/respiracion/personaje',
    status_code=status.HTTP_200_OK,
    response_model=respiraciones_personaje_schema.RespiracionesPersonaje,
    tags=['Respiraciones']
)
async def create_respiraciones_personajes(
    respiracion_personaje:respiraciones_personaje_schema.RespiracionesPersonaje = Body(...),
    token:str = Depends(get_current_active_user)
):  
    personaje_recived = seccion.query(personaje.Personaje).get(respiracion_personaje.id_personaje.strip())
    respiraciones_recived = seccion.query(respiraciones.Respiraciones).get(respiracion_personaje.id_respiracion.strip())
    
    personaje_recived.respiraciones.append(respiraciones_recived)
    respiraciones_recived.personajes.append(personaje_recived)
    
    seccion.commit()
    seccion.close()

    return respiracion_personaje


