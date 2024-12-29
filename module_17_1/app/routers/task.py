from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from module_17_1.app.backend.db_depends import get_db
from typing import Annotated
from module_17_1.app.models.user import User
from module_17_1.app.schemas import CreateUser, UpdateUser
from sqlalchemy import insert, select, update, delete
from slugify import slugify


from fastapi import APIRouter

router = APIRouter(prefix='/task', tags=['task'])


@router.get('/')
async def all_tasks():
    pass


@router.get('/task_id')
async def task_by_id():
    pass


@router.post('/create')
async def create_task():
    pass


@router.put('/update')
async def update_task():
    pass


@router.delete('/delete')
async def delete_task():
    pass

