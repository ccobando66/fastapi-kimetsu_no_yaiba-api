from pydantic import (
    BaseModel,Field
)


class Espada(BaseModel):
    id_espada:str = Field(
        default=None
    )
    color:str = Field(
        ...
    )
    danio:float = Field(
        ...,
        le=0
    )
    vida:float = Field(
        default=None,
        le=0  
    )
    
    
  
    