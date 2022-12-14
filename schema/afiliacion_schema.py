from pydantic import (
    BaseModel,Field
)

        
class Afiliacion(BaseModel):
    nombre:str = Field(
        ...,
        min_length=1
    )
    tipo_id:int = Field(
        ...,
        lg=0
    )
    
   
   