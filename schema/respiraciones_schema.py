from pydantic import (
    BaseModel,Field
)

class Naturaleza(BaseModel):
    id:int = Field(
        default=None
    )
    nombre:str = Field(
        ...,
        min_length=1
    )
    principal:str = Field(
        ...,
        min_length=1
    )
    
    

class Respiraciones(BaseModel):
    id:str = Field(
        default=None
    )
    nombre:str = Field(
        ...,
        min_length=1
    )
    id_naturaleza:int = Field(
        ...,
        lg=0
    )
    
    