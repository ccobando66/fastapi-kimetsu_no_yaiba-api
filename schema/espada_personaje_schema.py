from pydantic import(
    BaseModel, Field
)


class EspadaPersonaje(BaseModel):

    id_personaje:str = Field(
        ...,
        min_length=1
    )
    id_espada:str = Field(
        ...,
        min_length=1
    )
