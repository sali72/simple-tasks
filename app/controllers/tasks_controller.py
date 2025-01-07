from app.crud import TasksCRUD
from app.models import Task
from app.schemas import TaskCreationSchema, TaskUpdateSchema


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

    @classmethod
    async def get_tasks(cls) -> list[dict]:
        tasks = await TasksCRUD.get_tasks()
        return [task.to_dict() for task in tasks]

    @classmethod
    async def update_task(cls, task_id: int, task_schema: TaskUpdateSchema) -> Task:
        update_data = {
            key: value for key, value in task_schema.dict(exclude_unset=True).items()
        }

        # Update the task with only the provided fields
        updated_task = await TasksCRUD.update_task(task_id, update_data)
        return updated_task
    
    @classmethod
    async def delete_task(cls, task_id: int) -> None:
        await TasksCRUD.delete_task(task_id)
        return None
