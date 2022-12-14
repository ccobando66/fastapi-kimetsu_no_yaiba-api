from pydantic import (
    BaseModel,Field
)


class EspeciePersonaje(BaseModel):


    id_personaje:str = Field(
        ...,
        min_length=1
    )
    id_especie:int = Field(
        ...,
        lg=0
    )