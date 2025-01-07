from app.crud import TasksCRUD
from app.models import Task
from app.schemas import TaskCreationSchema


class TasksController:

    @classmethod
    async def create_task(cls, task_schema: TaskCreationSchema) -> str:
        task_model = await cls.__create_task_model(task_schema)
        result = await TasksCRUD.create_task(task_model)
        return str(result.id)

    @classmethod
    async def __create_task_model(cls, task_schema: TaskCreationSchema) -> Task:
        return Task(
            title=task_schema.title,
            description=task_schema.description,
            is_completed=task_schema.is_completed,
        )

    @classmethod
    async def get_task(cls, task_id: int) -> Task:
        return await TasksCRUD.get_task(task_id)
