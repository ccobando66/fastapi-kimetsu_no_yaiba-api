from fastapi import FastAPI
from routers import(
    personajes,respiraciones, espadas,
    especies,auth,tecnica,afiliacion
)


app = FastAPI()


app.include_router(personajes.personajes)
app.include_router(respiraciones.respiracion)
app.include_router(espadas.espadas)
app.include_router(especies.especies)
app.include_router(auth.auth)
app.include_router(tecnica.tecnicas)
app.include_router(afiliacion.afiliaciones)
