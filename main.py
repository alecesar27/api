from fastapi import FastAPI
from app.routes.routes import router as produtor_router

app = FastAPI()

# Inclui as rotas do produtor
app.include_router(produtor_router)




