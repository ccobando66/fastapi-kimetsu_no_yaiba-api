
from models import (
    personaje,especie,especie_personaje
   
)

from schema import(
   especie_schema, especie_personaje_schema
)

from helpers.get_especies_for_personaje import helpers_get_especie_personajes

from auth.Oauth2 import(
   get_current_active_user
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

especies = APIRouter()

@especies.get(
    path='/api/v1/especies',
    status_code=status.HTTP_200_OK,
    tags=['Especies']
)
async def get_all_especies(token:str = Depends(get_current_active_user)):
    query = seccion.query(especie.Especie).all()
    if len(query) < 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='No hay Especies registradas')
    return query


@especies.get(
    path='/api/v1/especies/personaje/{id_personaje}',
    status_code=status.HTTP_200_OK,
    tags=['Especies']
)
async def get_especie_personajes(
    id_personaje:str = Path(...),
    token:str = Depends(get_current_active_user)
):
   
    return helpers_get_especie_personajes(id_personaje)



@especies.post(
    path='/api/v1/especies/',
    status_code=status.HTTP_200_OK,
    tags=['Especies']
)
async def create_especies(
    especies:especie_schema.Especie = Body(...),
    token:str = Depends(get_current_active_user)
):  
   
    
    especie_recived = especie.Especie(
        nombre =  especies.nombre.strip(),
    )
    seccion.add(especie_recived) 
    seccion.commit()
    seccion.close()
    
    return {'sms':'Especie Creada'}


@especies.post(
    path='/api/v1/especies/personaje',
    status_code=status.HTTP_200_OK,
    response_model=especie_personaje_schema.EspeciePersonaje,
    tags=['Especies']
)
async def create_especies_personajes(
    especie_personaje: especie_personaje_schema.EspeciePersonaje = Body(...),
    token:str = Depends(get_current_active_user)
):  
    try:
        personaje_recived = seccion.query(personaje.Personaje).get(especie_personaje.id_personaje.strip())
        especie_recived = seccion.query(especie.Especie).get(especie_personaje.id_especie)
        personaje_recived.especies.append(especie_recived)
        especie_recived.personajes.append(personaje_recived) 
        seccion.commit()
        seccion.close()
        return especie_personaje
    except  Exception as ex:
        print(ex)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='datos incorrectos, por favor verifique los datos enviados')    

    






