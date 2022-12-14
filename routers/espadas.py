from typing import List

import uuid

from auth.Oauth2 import(
   get_current_active_user
)

from models import (
    personaje,espada
   
)

from schema import(
   espada_schema,espada_personaje_schema
)

from helpers import(
    get_espadas_for_personaje
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

espadas = APIRouter()

@espadas.get(
    path='/api/v1/espadas',
    status_code=status.HTTP_200_OK,
    tags=['Espadas']
)
async def get_all_espadas(token:str = Depends(get_current_active_user)):
    query = seccion.query(espada.Espada).filter(espada.Espada.vida > 0).all()
    if query is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='No hay Espadas registradas')
    return query

@espadas.get(
    path='/api/v1/espadas/danadas',
    status_code=status.HTTP_200_OK,
    tags=['Espadas']
)
async def get_all_espadas(token:str = Depends(get_current_active_user)):
    query = seccion.query(espada.Espada).filter(espada.Espada.vida == 0).all()
    if query is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='No hay Espadas averiadas')
    return query



@espadas.get(
    path='/api/v1/espadas/{id_espadas}',
    status_code=status.HTTP_200_OK,
    tags=['Espadas']
)
async def get_espadas(
    id_espadas:str = Path(...),
    token:str = Depends(get_current_active_user)
):
    query = seccion.query(espada.Espada).get(id_espadas.strip())
    if query is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='no existe la espada')
    return query


@espadas.get(
    path='/api/v1/espadas/personaje/{id_personaje}',
    status_code=status.HTTP_200_OK,
    tags=['Espadas']
)
async def get_espadas_personajes(
    id_personaje:str = Path(...),
    token:str = Depends(get_current_active_user)
):
    response = get_espadas_for_personaje.helpers_get_espadas_personajes(id_personaje)
    return response



@espadas.post(
    path='/api/v1/espadas/',
    status_code=status.HTTP_200_OK,
    response_model=espada_schema.Espada,
    tags=['Espadas']
)
async def create_Espadas(
    espadas:espada_schema.Espada = Body(...),
    token:str = Depends(get_current_active_user)
):  
    espadas.id_espada = str(uuid.uuid4())
    
    espada_recived = espada.Espada(
        id_espada = espadas.id_espada,
        color =  espadas.color.strip(),
        danio = espadas.danio
    )
    seccion.add(espada_recived) 
    seccion.commit()
    seccion.close()
    return espadas

@espadas.post(
    path='/api/v1/espadas/personaje',
    status_code=status.HTTP_200_OK,
    tags=['Espadas']
)
async def create_espada_personajes(
    espada_personaje:espada_personaje_schema.EspadaPersonaje = Body(...),
    token:str = Depends(get_current_active_user)
    
):  
    try:
        personaje_recived = seccion.query(personaje.Personaje).get(espada_personaje.id_personaje.strip())
        espadas_recived = seccion.query(espada.Espada).get(espada_personaje.id_espada.strip())
        get_katana_by_personaje = get_espadas_for_personaje.helpers_get_espadas_personajes(espada_personaje.id_personaje)
        
    
        if len(get_katana_by_personaje)<=0:
            personaje_recived.espadas.append(espadas_recived)
            espadas_recived.personajes.append(personaje_recived)
            seccion.commit()
            seccion.close()
            return {'katana':'katana asignada'}
        elif (len(get_espadas_for_personaje.helpers_get_espadas_personajes(espada_personaje.id_personaje)) > 0) and personaje_recived.nombre == 'Tanjirō':
            katanas_danadas = 0
            for value in range(len(get_katana_by_personaje)):
                if get_katana_by_personaje[value][2] >= 100:
                      katanas_danadas +=1
                      
                      if get_katana_by_personaje[value][0] == espada_personaje.id_espada.strip():
                           return {'sms': 'la katana ya fue asignada, por favor seleccione otra'}   
                       
                      if katanas_danadas < 2 and value == len(get_katana_by_personaje) - 1 and get_katana_by_personaje[value][0] != espada_personaje.id_espada.strip():
                          personaje_recived.espadas.append(espadas_recived)
                          espadas_recived.personajes.append(personaje_recived)
                          seccion.commit()
                          seccion.close()
                          return {'sms': 'su katana esta dañada o perdida, haganezuka esta enfadado, mira su reacion enlace: https://www.youtube.com/shorts/xXY-2CQxQaU'}
                      
                      elif katanas_danadas < 3 and value == len(get_katana_by_personaje) - 1 and get_katana_by_personaje[value][0] != espada_personaje.id_espada.strip() :
                          personaje_recived.espadas.append(espadas_recived)
                          espadas_recived.personajes.append(personaje_recived)
                          seccion.commit()
                          seccion.close()
                          return {'sms': 'su katana esta dañada o perdida otra vez, haganezuka esta enfadado, mira su reacion enlace: https://www.youtube.com/watch?v=p4C2q56W8aE'}
                      
                      elif katanas_danadas >= 3 and value == len(get_katana_by_personaje) - 1 and get_katana_by_personaje[value][0] != espada_personaje.id_espada.strip():
                        return {'sms': 'ha dañado o perdido mas de 2 katana, haganezuka esta enfadado, mira el mensaje que te dejo: https://pbs.twimg.com/media/EFo6BEZXUAAcq8D.jpg'} 
            else:
              return {'sms': f'hola {personaje_recived.nombre}, su katana esta en buen estado '}    
        else:
            return {'sms': f'hola {personaje_recived.nombre}, su katana esta en buen estado'} 
    except  Exception as ex:
        print(ex)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='datos incorrectos, por favor verifique los datos enviados')    

    






