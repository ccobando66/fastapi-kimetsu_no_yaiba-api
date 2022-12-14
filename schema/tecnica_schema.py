from pydantic import (
    BaseModel,Field
)

class Tecnica(BaseModel):
    id:str = Field(
        default=None,
    )
    nombre:str = Field(
        default=None,
        min_length=1
    )
    danio:float = Field(
        default=None,
        lg=0
    )
    id_personaje:str = Field(
        default=None,
    ) 
    
    