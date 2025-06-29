from sqlmodel import Session, select
from app.models import Task
from app.schemas import TaskCreate, TaskUpdate
from datetime import datetime
from typing import List

def create_task(session: Session, task_data: TaskCreate) -> Task:
    task = Task.from_orm(task_data)
    session.add(task)
    session.commit()
    session.refresh(task)
    return task

def get_task(session: Session, task_id: int) -> Task:
    return session.get(Task, task_id)

def get_all_tasks(session: Session, skip: int = 0, limit: int = 10) -> List[Task]:
    return session.exec(select(Task).offset(skip).limit(limit)).all()

def update_task(session: Session, task: Task, updates: TaskUpdate) -> Task:
    task_data = updates.dict(exclude_unset=True)  # only fields that were provided
    for key, value in task_data.items():
        setattr(task, key, value)
    task.updated_at = datetime.utcnow()
    session.add(task)
    session.commit()
    session.refresh(task)
    return task

def delete_task(session: Session, task: Task):
    session.delete(task)
    session.commit()
