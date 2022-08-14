from typing import List

from fastapi import APIRouter

import api.schemas.task as task_schema

router = APIRouter()

@router.get("/tasks")
async def list_tasks():
  return [task_scheme.Task(id=1, title="１つ目のタスク")]

@router.post("/tasks", response_model = task_schema.TaskCreateResponse)
async def create_task(task_body: task_schema.TaskCreate):
  return task_schema.TaskCreateResponse(id= 1, **task_body.dict())

@router.get("/tasks/{task_id}")
async def update_task():
  pass

@router.get("/tasks/{task_id}")
async def delete_task():
  pass