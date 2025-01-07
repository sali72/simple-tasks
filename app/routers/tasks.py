from fastapi import APIRouter

from app.controllers.tasks_controller import TasksController
from app.schemas import ResponseSchema, TaskCreationSchema, TaskUpdateSchema

tasks_router = APIRouter(prefix="/tasks", tags=["Tasks"])


@tasks_router.post("", response_model=ResponseSchema)
async def create_task_route(task_schema: TaskCreationSchema):
    """Create a new task.

    Args:
        task_schema (TaskCreationSchema): The schema containing the task details.
            - title (str): The task title.
            - is_completed (bool): The task completion status. Defaults to False.
            - description (str): The task description. Optional.

    Returns:
        ResponseSchema: A response containing the ID of the created task and a success message.
            - message (str): A success message.
            - data (dict): Contains the ID of the created task.
    """
    _id = await TasksController.create_task(task_schema)

    message = "Task created successfully"
    data = {"id": _id}
    return ResponseSchema(data=data, message=message)


@tasks_router.get("/{task_id}", response_model=ResponseSchema)
async def get_task_route(task_id: int):
    """Retrieve a task by its ID.

    Args:
        task_id (int): The ID of the task to retrieve.

    Returns:
        ResponseSchema: A response containing the task details and a success message.
            - message (str): A success message.
            - data (dict): Contains the task details.
                - title (str): The task title.
                - is_completed (bool): The task completion status.
                - description (str): The task description.
                - created_at (datetime): The timestamp when the task was created.
    """
    task = await TasksController.get_task(task_id)

    message = "Task retrieved successfully"
    data = task.to_dict()
    return ResponseSchema(data=data, message=message)


@tasks_router.get("", response_model=ResponseSchema)
async def get_tasks_route():
    """Retrieve all tasks.

    Returns:
        ResponseSchema: A response containing a list of all tasks and a success message.
            - message (str): A success message.
            - data (dict): Contains a list of tasks.
                - Each task includes:
                    - title (str): The task title.
                    - is_completed (bool): The task completion status.
                    - description (str): The task description.
                    - created_at (datetime): The timestamp when the task was created.
    """
    tasks = await TasksController.get_tasks()

    message = "Tasks retrieved successfully"
    data = {"tasks": tasks}
    return ResponseSchema(data=data, message=message)


@tasks_router.put("/{task_id}", response_model=ResponseSchema)
async def update_task_route(task_id: int, task_schema: TaskUpdateSchema):
    """Update a task by its ID.

    Args:
        task_id (int): The ID of the task to update.
        task_schema (TaskUpdateSchema): The schema containing the updated task details.
            - title (Optional[str]): The task title. Optional.
            - is_completed (Optional[bool]): The task completion status. Optional.
            - description (Optional[str]): The task description. Optional.

    Returns:
        ResponseSchema: A response containing the updated task details and a success message.
            - message (str): A success message.
            - data (dict): Contains the updated task details.
    """
    task = await TasksController.update_task(task_id, task_schema)

    message = "Task updated successfully"
    data = task.to_dict()
    return ResponseSchema(data=data, message=message)


@tasks_router.delete("/{task_id}", response_model=ResponseSchema)
async def delete_task_route(task_id: int):
    """Delete a task by its ID.

    Args:
        task_id (int): The ID of the task to delete.

    Returns:
        ResponseSchema: A response containing a success message.
            - message (str): A success message.
    """
    await TasksController.delete_task(task_id)

    message = "Task deleted successfully"
    return ResponseSchema(message=message)