from passlib.hash import bcrypt
import jwt
from datetime import datetime

from fastapi import(
    Depends ,HTTPException, status
) 

from fastapi.security import (
  OAuth2PasswordBearer, OAuth2PasswordRequestForm   
)

from config.config import(
    conexion,Seccion,Base
)

from models.usuario import Ususario
from schema.usuario_schema import Ususario as usuario_schema, UsusarioPasswd


from decouple import config

JWT_SECRET = config('SECRET_KEY')
JWT_ALGORITM = config('ALGORITMH')

#conexion a base de datos 
Base.metadata.create_all(conexion)
seccion = Seccion()

#generando la autorizacion
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token/jwt')

def get_user(username:str):
    query = seccion.query(
        Ususario.id,
        Ususario.username,
        Ususario.email,
        Ususario.disable,
        Ususario.passwd,
        Ususario.expiration
        ).filter(Ususario.username == username).first()
    return query

def decode_jwt(token:str):
    payload = jwt.decode(token,JWT_SECRET,algorithms=JWT_ALGORITM)
    return payload['username']

 

async def get_current_user(token:str = Depends(oauth2_scheme)):
    get_payload = decode_jwt(token=token)
    user = get_user(get_payload)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Invalid authentication credentials',
            headers={"WWW-Authenticate": "Bearer"}
        )
        
    data_actual = datetime.utcnow()    
    if data_actual >= user.expiration:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='token expirated, please renew token',
            headers={"WWW-Authenticate": "Bearer"}
        )
    return user

async def get_current_active_user(current_user:usuario_schema = Depends(get_current_user)):
    if current_user.disable:
          raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Inactive User'
        )
    return current_user




       

