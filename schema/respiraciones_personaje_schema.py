from pydantic import (
    BaseModel,Field
)

class RespiracionesPersonaje(BaseModel):
    id_personaje:str = Field(
        ...,
        min_length=1
    )
    id_respiracion:str = Field(
        ...,
        min_length=1
    )

class RespiarcionesDePersonajes(BaseModel):
    nombre: str
    respiracion: str
    principal:str 
