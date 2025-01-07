from app.database import db_session as db
from app.models import Task


class TasksCRUD:

    @classmethod
    async def create_task(cls, task: Task) -> Task:
        db.add(task)
        db.commit()
        db.refresh(task)
        return task
