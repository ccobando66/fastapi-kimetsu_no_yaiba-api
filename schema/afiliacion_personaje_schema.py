from pydantic import (
    BaseModel,Field
)



class AfiliacionPersonaje(BaseModel):
    id_personaje:str = Field(
        ...,
        min_length=1
    )
    id_afiliacion:int = Field(
        ...,
        lg=0
    )
