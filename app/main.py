from fastapi import FastAPI, HTTPException

from app.database import Base, engine
from app.routers.tasks import tasks_router
from commons.exception_handlers import base_exception_handler, http_exception_handler

Base.metadata.create_all(engine)

app = FastAPI(
    title="Simple Tasks API",
    description=(
        "This API allows you to manage tasks, including creating, updating, "
        "retrieving, and deleting tasks. It is designed to be simple and easy to use."
    ),
    version="0.1.0",
    contact={
        "name": "Seyed Ali Hashemi",
        "email": "sahashemi072@gmail.com",
    },
    license_info={
        "name": "MIT License",
        "url": "https://opensource.org/licenses/MIT",
    },
)

app.include_router(tasks_router)

app.add_exception_handler(HTTPException, http_exception_handler)
app.add_exception_handler(Exception, base_exception_handler)
