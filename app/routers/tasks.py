from fastapi import APIRouter

from app.controllers.tasks_controller import TasksController
from app.schemas import ResponseSchema, TaskCreationSchema

tasks_router = APIRouter(prefix="/task", tags=["Tasks"])


@tasks_router.post("", response_model=ResponseSchema)
async def create_task_route(task_schema: TaskCreationSchema):
    _id = await TasksController.create_task(task_schema)

    message = "Task created successfully"
    data = {"id": _id}
    return ResponseSchema(data=data, message=message)
