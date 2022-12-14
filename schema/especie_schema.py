from pydantic import (
    BaseModel,Field
)


class Especie(BaseModel):
    id:int = Field(
        default=None
    )
    nombre:str = Field(
        ...
    )
    vida:float = Field(
        default=None,
        lg=0
    )
    
    
    
  

