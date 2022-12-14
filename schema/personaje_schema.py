from pydantic import (
    BaseModel,Field
)

class Personaje(BaseModel):
    id_personaje:str = Field(
        default=None
    )
    nombre:str = Field(
        ...,
        min_length=1
    )
    apellido:str = Field(
        ...,
        min_length=1
        
    )
    edad:int = Field(
        ...,
        lg=0
    )
    resistencia:float = Field(
        ...,
        lg=0
    )
    poder:float = Field(
        ...,
        lg=0
    )
    
    