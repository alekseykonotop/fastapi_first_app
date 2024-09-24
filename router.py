from fastapi import APIRouter
from fastapi import Depends
from typing import Annotated
from schemas import STaskAdd, STask, STaskId, SUserAdd, SUser, SUserId
from repository import TaskRepository, UserRepository

router = APIRouter(
    tags=['MAIN ROOTS'],
)

users_router = APIRouter(
    prefix="/users",
    tags=["USERS"],
)
tasks_router = APIRouter(
    prefix="/tasks",
    tags=["TASKS"],
)


# MAIN ROOTS
@router.get("/")
def get_root_page():
    return {'message': 'Hello from ROOT page!'}


@router.get("/home")
def get_home_page():
    return {'message': 'Hello from HOME page!'}


# TASKS
@tasks_router.post("")
async def add_task(
        task: Annotated[STaskAdd, Depends()]
) -> STaskId:
    task_id = await TaskRepository.add_one(task)

    return {'ok': True, 'task_id': task_id}


@tasks_router.get("")
async def get_tasks() -> list[STask]:
    tasks = await TaskRepository.find_all()
    return tasks


# USERS
@users_router.post("")
async def add_user(
        user: Annotated[SUserAdd, Depends()]
) -> SUserId:
    user_id = await UserRepository.add_user(user)

    return {"Success": True, "user_id": user_id}


@users_router.get("")
async def find_all_users() -> list[SUser]:
    users = await UserRepository.find_all()

    return users


@users_router.get("/{user_id}")
async def get_user_data(user_id: int) -> SUser:

    user = await UserRepository.find_user(user_id)
    return user



