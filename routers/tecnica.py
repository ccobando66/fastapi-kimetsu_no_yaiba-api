from typing import List

import uuid

from auth.Oauth2 import(
   get_current_active_user
)

from models import (
    personaje,tecnica
   
)

from schema import(
   tecnica_schema,personaje_schema
)

from helpers import(
    get_especies_for_personaje
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

tecnicas = APIRouter()

@tecnicas.get(
    path='/api/v1/tecnicas',
    status_code=status.HTTP_200_OK,
    tags=['Tecnicas']
)
async def get_all_tecnicas(token:str = Depends(get_current_active_user)):
    query = seccion.query(tecnica.Tecnica).all()
    if len(query) <=0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='No hay Tecnicas registradas')
    return query

@tecnicas.get(
    path='/api/v1/tecnicas/{id_tecnica}',
    status_code=status.HTTP_200_OK,
    tags=['Tecnicas']
)
async def get_tecnicas(
    id_tecnica:str = Path(...),
    token:str = Depends(get_current_active_user)
):
    query = seccion.query(tecnica.Tecnica).get(id_tecnica.strip())
    if query is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='no existe la tecnica')
    return query


@tecnicas.get(
    path='/api/v1/tecnicas/personaje/{id_personaje}',
    status_code=status.HTTP_200_OK,
    tags=['Tecnicas']
)
async def get_espadas_personajes(
    id_personaje:str = Path(...),
    token:str = Depends(get_current_active_user)
):
    response = seccion.query(tecnica.Tecnica).filter(tecnica.Tecnica.personaje == id_personaje).all()
    if len(response)<=0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="no tienes tecnicas registradas"
        )
    return response


@tecnicas.post(
    path='/api/v1/tecnicas/',
    status_code=status.HTTP_200_OK,
    response_model=tecnica_schema.Tecnica,
    tags=['Tecnicas']
)
async def create_tecnicas(
    tecnicas:tecnica_schema.Tecnica = Body(...),
    token:str = Depends(get_current_active_user)
):  
    tecnicas.id = str(uuid.uuid4())
    
    tecnica_recived = tecnica.Tecnica(
        id = tecnicas.id,
        nombre = tecnicas.nombre.strip(),
        danio = tecnicas.danio
    )
    seccion.add(tecnica_recived) 
    seccion.commit()
    seccion.close()
    return tecnicas

@tecnicas.post(
    path='/api/v1/tecnicas/personaje',
    status_code=status.HTTP_200_OK,
    tags=['Tecnicas']
)
async def create_tecnicas_personajes(
    tecnicas:tecnica_schema.Tecnica = Body(...),
    token:str = Depends(get_current_active_user)
    
):  
    
    personaje_recived = seccion.query(personaje.Personaje).get(tecnicas.id_personaje.strip())
    get_especie = get_especies_for_personaje.helpers_get_especie_personajes(tecnicas.id_personaje.strip())
    tecnica_recived = seccion.query(tecnica.Tecnica).get(tecnicas.id)       
    
    if len(get_especie)<=0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="no tiene especie asignada,por favor asignele una para continuar"
        )
    else:
        for value in range(len(get_especie)):
            if get_especie[value][0] != 'Demonio' or get_especie[value][2] == False:
                raise HTTPException(
                      status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                      detail=f"Eres {get_especie[value][0]}, estas tecnicas va orientadas a Raza Demoniaca "
                )
                
    if tecnica_recived.personaje is not None:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="La tecnica ya fue asignada a un demonio,por favor ingrese otra tecnica"
        )
    
    if tecnica_recived.personaje is not None:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="No existe esa tecnica, por favor seleccione una"
        )
        
            
    
    personaje_recived.tecnicas.append(tecnica_recived)
    seccion.commit()
    seccion.close()
    
    return {'sms':'personaje'}
        

        
    
        

    