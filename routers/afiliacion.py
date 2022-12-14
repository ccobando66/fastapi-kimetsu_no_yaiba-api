from typing import List

import uuid

from auth.Oauth2 import(
   get_current_active_user
)

from models import (
    personaje,afiliacion,afiliacion_personaje
   
)

from schema import(
   afiliacion_schema, afiliacion_personaje_schema
)

from helpers import(
    get_afiliacion_for_personaje,
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

afiliaciones = APIRouter()

@afiliaciones.get(
    path='/api/v1/afiliacion',
    status_code=status.HTTP_200_OK,
    tags=['Afiliaciones']
)
async def get_all_tecnicas(token:str = Depends(get_current_active_user)):
    query = seccion.query(afiliacion.Afiliacion).all()
    if len(query) <=0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='No hay Afiliaciones registradas')
    return query

"""
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

"""
@afiliaciones.get(
    path='/api/v1/afiliacion/personaje/{id_personaje}',
    status_code=status.HTTP_200_OK,
    tags=['Afiliaciones']
)
async def get_espadas_personajes(
    id_personaje:str = Path(...),
    token:str = Depends(get_current_active_user)
):
    response = get_afiliacion_for_personaje.helpers_get_afiliacion_personajes(id_personaje.strip())
    if len(response)<=0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="no tienes afiliaciones registradas"
        )
    return response


@afiliaciones.post(
    path='/api/v1/afiliacion/',
    status_code=status.HTTP_200_OK,
    response_model=afiliacion_schema.Afiliacion,
    tags=['Afiliaciones']
)
async def create_afiliacion(
    afiliaciones:afiliacion_schema.Afiliacion = Body(...),
    token:str = Depends(get_current_active_user)
):  
    tipo = seccion.query(afiliacion.Tipo).get(afiliaciones.tipo_id)
    afiliacion_recived = afiliacion.Afiliacion(
        nombre = afiliaciones.nombre.upper().strip(),
        
    )
    if tipo is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='el tipo ingresado, no esta registrado')

    seccion.add(afiliacion_recived) 
    afiliacion_recived.rel_tipo = tipo
    seccion.commit()
    seccion.close()
    return afiliaciones


@afiliaciones.post(
    path='/api/v1/afiliacion/personaje',
    status_code=status.HTTP_200_OK,
    tags=['Afiliaciones']
)
async def create_afiliacion_personajes(
    afiliaciones:afiliacion_personaje_schema.AfiliacionPersonaje = Body(...),
    token:str = Depends(get_current_active_user)
    
):  
    
    personaje_recived = seccion.query(personaje.Personaje).get(afiliaciones.id_personaje.strip())
    get_especie = get_especies_for_personaje.helpers_get_especie_personajes(afiliaciones.id_personaje.strip())
    afiliacion_recived = seccion.query(afiliacion.Afiliacion).get(afiliaciones.id_afiliacion)       
    
    if len(get_especie)<=0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="no tiene especie asignada,por favor asignele una para continuar"
        )
    
    result = list(filter(lambda lista: lista[0] != 'Humano' and lista[2] == True, get_especie))
    
           
    if afiliacion_recived is None:
        
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="No existe esa afiliacion, por favor seleccione una"
        )
        
    if  len(result)<=0 and afiliacion_recived.nombre.find('LUNA') == 0:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=f"Eres un {get_especie[0][0]}, esta raza no pertenece a las 12 lunas demoniacas"
        ) 
    
    if  len(result)>0 and afiliacion_recived.nombre.find('LUNA') != 0:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=f"Eres un {result[0][0]}, esta raza no pertenece al Cuerpo de Exterminio de Demonios"
        ) 
          
    personaje_recived.afiliaciones.append(afiliacion_recived)
    afiliacion_recived.personajes.append(personaje_recived)
    seccion.commit()
    seccion.close()
    
    return {'sms':'personaje afiliado'}
      

        
    
        

    