from commons.exception_handlers import base_exception_handler, http_exception_handler
from fastapi import FastAPI, HTTPException

from app.database import Base, engine
from app.routers.tasks import tasks_router

Base.metadata.create_all(engine)

app = FastAPI()

app.include_router(tasks_router)

app.add_exception_handler(HTTPException, http_exception_handler)
app.add_exception_handler(Exception, base_exception_handler)
