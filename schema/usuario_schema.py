from pydantic import (
    BaseModel,Field
)


class Ususario(BaseModel):

    username:str = Field(
        ...,
        min_length=1
    )
    email:str = Field(
        default=None, 
        min_length=1
    )
    disable:bool = Field(
        default=False
    )


class UsusarioPasswd(Ususario):
    passwd:str = Field(
        ...,
        min_length=8,
        example='password is here'
    )