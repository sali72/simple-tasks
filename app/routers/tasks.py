from fastapi import APIRouter

from app.controllers.tasks_controller import TasksController
from app.schemas import ResponseSchema, TaskCreationSchema, TaskUpdateSchema

tasks_router = APIRouter(prefix="/tasks", tags=["Tasks"])


@tasks_router.post("", response_model=ResponseSchema)
async def create_task_route(task_schema: TaskCreationSchema):
    _id = await TasksController.create_task(task_schema)

    message = "Task created successfully"
    data = {"id": _id}
    return ResponseSchema(data=data, message=message)


@tasks_router.get("/{task_id}", response_model=ResponseSchema)
async def get_task_route(task_id: int):
    task = await TasksController.get_task(task_id)

    message = "Task retrieved successfully"
    data = task.to_dict()
    return ResponseSchema(data=data, message=message)


@tasks_router.get("", response_model=ResponseSchema)
async def get_tasks_route():
    tasks = await TasksController.get_tasks()

    message = "Tasks retrieved successfully"
    data = {"tasks": tasks}
    return ResponseSchema(data=data, message=message)

@tasks_router.put("/{task_id}", response_model=ResponseSchema)
async def update_task_route(task_id: int, task_schema: TaskUpdateSchema):
    task = await TasksController.update_task(task_id, task_schema)

    message = "Task updated successfully"
    data = task.to_dict()
    return ResponseSchema(data=data, message=message)