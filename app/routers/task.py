from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.backend.db_depends import get_db
from typing import Annotated
from app.models import Task
from app.schemas import CreateTask, UpdateTask
from sqlalchemy import insert, select, update, delete
from slugify import slugify

router = APIRouter(prefix="/task", tags=["task"])

@router.get("/")
async def all_tasks():
    pass

@router.get('/task_id')
async def task_by_id(task_id):
    pass

@router.post('/create')
async def create_task(title, content, priority):
    pass

@router.put('/update')
async def update_task(task_id, title, content, priority):
    pass

@router.delete('/delete')
async def delete_task(task_id):
    pass

# from sqlalchemy.schema import CreateTable
# print(CreateTable(Task.__table__))