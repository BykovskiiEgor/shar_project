from fastapi import FastAPI
from api.v1 import routers


app = FastAPI()


app.include_router(routers)

