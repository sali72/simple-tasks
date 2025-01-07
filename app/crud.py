from sqlalchemy import update
from sqlalchemy.exc import NoResultFound
from sqlalchemy.future import select

from app.database import db_session as db
from app.models import Task


class TasksCRUD:

    @classmethod
    async def create_task(cls, task: Task) -> Task:
        db.add(task)
        db.commit()
        db.refresh(task)
        return task

    @classmethod
    async def get_task(cls, task_id: int) -> Task:
        task = db.query(Task).filter(Task.id == task_id).first()
        if task is None:
            raise NoResultFound(f"Task with id {task_id} does not exist.")
        return task

    @classmethod
    async def get_tasks(cls) -> list[Task]:
        return db.query(Task).all()

    @classmethod
    async def update_task(cls, task_id: int, update_data: dict) -> Task:
        stmt = (
            update(Task)
            .where(Task.id == task_id)
            .values(**update_data)
            .execution_options(synchronize_session="fetch")
        )
        db.execute(stmt)
        db.commit()

        stmt = select(Task).where(Task.id == task_id)
        result = db.execute(stmt)
        return result.scalar_one_or_none()

    @classmethod
    async def delete_task(cls, task_id: int) -> None:
        result = db.query(Task).filter(Task.id == task_id).delete()
        db.commit()

        if result == 0:
            raise NoResultFound(f"Task with id {task_id} does not exist.")
