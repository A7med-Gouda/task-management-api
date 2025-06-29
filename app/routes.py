from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from typing import List
from app.schemas import TaskCreate, TaskUpdate, TaskResponse
from app.database import get_session
from app.crud import create_task, get_task, get_all_tasks, update_task, delete_task
from app.models import Task, TaskStatus, TaskPriority

router = APIRouter()

@router.get("/", tags=["Root"])
def root():
    return {"message": "Task Management API", "endpoints": ["/tasks", "/tasks/{task_id}"]}

@router.get("/health", tags=["Health"])
def health():
    return {"status": "ok"}

@router.post("/tasks", response_model=TaskResponse, status_code=201)
def create(task: TaskCreate, session: Session = Depends(get_session)):
    return create_task(session, task)

@router.get("/tasks", response_model=List[TaskResponse])
def list_tasks(skip: int = 0, limit: int = 10, session: Session = Depends(get_session)):
    return get_all_tasks(session, skip, limit)

@router.get("/tasks/{task_id}", response_model=TaskResponse)
def retrieve(task_id: int, session: Session = Depends(get_session)):
    task = get_task(session, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.put("/tasks/{task_id}", response_model=TaskResponse)
def update(task_id: int, task_data: TaskUpdate, session: Session = Depends(get_session)):
    task = get_task(session, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return update_task(session, task, task_data)

# Delete all tasks
@router.delete("/tasks", status_code=status.HTTP_204_NO_CONTENT)
def delete_all_tasks(session: Session = Depends(get_session)):
    session.exec(select(Task)).all()
    session.exec("DELETE FROM task")
    session.commit()
    return

@router.delete("/tasks/{task_id}", status_code=204)
def delete(task_id: int, session: Session = Depends(get_session)):
    task = get_task(session, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    delete_task(session, task)
    return

# Filter by Status
@router.get("/tasks/status/{status}", response_model=List[TaskResponse])
def get_tasks_by_status(status: TaskStatus, session: Session = Depends(get_session)):
    tasks = session.exec(select(Task).where(Task.status == status)).all()
    return tasks


# Filter by Priority
@router.get("/tasks/priority/{priority}", response_model=List[TaskResponse])
def get_tasks_by_priority(priority: TaskPriority, session: Session = Depends(get_session)):
    tasks = session.exec(select(Task).where(Task.priority == priority)).all()
    return tasks

# 
@router.get("/tasks/search", response_model=List[TaskResponse])
def search_tasks(q: str, session: Session = Depends(get_session)):
    query = select(Task).where(
        Task.title.contains(q) | Task.description.contains(q)
    )
    results = session.exec(query).all()
    return results
