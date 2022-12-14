import jwt


from datetime import(
    datetime, timedelta
)

from .Oauth2 import get_user
from models.usuario  import Ususario

from config.config import(
    conexion,Base,Seccion
)

from decouple import config

JWT_SECRET = config('SECRET_KEY')
JWT_ALGORITM = config('ALGORITMH')
TIME_EXPIRATION = config('ACCESS_TOKEN_EXPIRE_MINUTES')

Base.metadata.create_all(conexion)
seccion = Seccion()


def get_token(token:str):
    return {
        'user_token':token
    }
    
def create_user_token(username:str):
    data = get_user(username)
    user_update = seccion.query(Ususario).get(data[0])
    data_exp = datetime.utcnow() + timedelta(minutes=int(TIME_EXPIRATION))
    data_actual = datetime.utcnow()
    server_token = user_update.token
    if data_actual >= user_update.expiration:
        payload = {
            'username': user_update.username,
            'expiration_token': data_exp.isoformat()
        }
        
        token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITM)
        user_update.token = token
        user_update.expiration = payload['expiration_token']
        seccion.add(user_update)
        seccion.commit()
        seccion.close()
        return token
    
    return server_token



