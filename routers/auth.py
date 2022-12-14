from fastapi import (
    APIRouter,status, Depends, HTTPException
)

from auth.Oauth2 import(
    OAuth2PasswordRequestForm,get_user,usuario_schema,get_current_active_user
)

from auth.JWT import (
    create_user_token
)

auth = APIRouter()

@auth.get(
    path='/token/me',
    tags=['Auth'],
    status_code=status.HTTP_200_OK
)
async def read_user_me(current_user:usuario_schema = Depends(get_current_active_user)):
    return current_user




@auth.post(
    path='/token/jwt',
    tags=['Auth'],
    status_code=status.HTTP_200_OK
)
async def create_jwt(form_data: OAuth2PasswordRequestForm = Depends()):
    user = get_user(form_data.username)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='invalid username'
        )
    if user.passwd != form_data.password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='invalid passwd'
        )
    create_token = create_user_token(form_data.username)   
    return {"access_token": create_token, "token_type": "bearer"} 
