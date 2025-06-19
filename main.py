from fastapi import FastAPI
from api.routes import router
import  models
from database import engine

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(router)