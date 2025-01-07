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
        return db.query(Task).filter(Task.id == task_id).first()
    
    @classmethod
    async def get_tasks(cls) -> list[Task]:
        return db.query(Task).all()
    
    @classmethod
    async def update_task(cls, task_id: int, task: Task) -> Task:
        db.query(Task).filter(Task.id == task_id).update(task.to_dict())
        db.commit()
        return task
    
    @classmethod
    async def delete_task(cls, task_id: int) -> None:
        db.query(Task).filter(Task.id == task_id).delete()
        db.commit()
        return None
