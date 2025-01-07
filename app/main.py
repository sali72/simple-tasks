from app.database import Base, engine
from fastapi import FastAPI

from app.routers.tasks import tasks_router

Base.metadata.create_all(engine)


app = FastAPI()

app.include_router(tasks_router)
