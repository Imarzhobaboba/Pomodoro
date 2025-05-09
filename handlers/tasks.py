from typing import Annotated

from fastapi import APIRouter, HTTPException,status, Depends

from dependency import get_tasks_repository, get_tasks_cache_repository, get_task_service, get_request_user_id
from exception import TaskNotFound
from schema.task import Task, TaskCreateSchema
from repository import TaskRepository, TaskCache

# from database.database import get_db_connection
from database.database import get_db_session
from service.task import TaskService


router = APIRouter(prefix="/task", tags=["task"])



@router.get(
        "/all",
        response_model=list[Task]
)
async def get_tasks(
    task_repository: Annotated[TaskRepository, Depends(get_tasks_repository)],
    task_cache: Annotated[TaskCache, Depends(get_tasks_cache_repository)]
):
    if tasks := task_cache.get_tasks():
        return tasks
    else:
        
        tasks = task_repository.get_tasks()
        tasks_schema = [Task.model_validate(task) for task in tasks]

        task_cache.set_tasks(tasks_schema)
        return tasks_schema


@router.post(
        "/",
        response_model=Task
)
async def create_task(
    body: TaskCreateSchema,
    task_service: Annotated[TaskService, Depends(get_task_service)],
    user_id: int = Depends(get_request_user_id)
):
    task = task_service.create_task(body, user_id)
    return task
        


@router.patch(
    "/{task_id}",
    response_model=Task
)
async def patch_task(
    task_id: int, 
    name: str,
    task_service: Annotated[TaskService, Depends(get_task_service)],
    user_id: int = Depends(get_request_user_id)
):
    try:
        return task_service.update_task_name(task_id=task_id, name=name, user_id=user_id)
    except TaskNotFound as e:
        raise HTTPException(
            status_code=404,
            detail=e.detail
        )



@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(
    task_id:int,
    task_service: Annotated[TaskService, Depends(get_task_service)],
    user_id: int = Depends(get_request_user_id)
):    
    try:
        task_service.delete_task(task_id=task_id, user_id=user_id)
    except TaskNotFound as e:
        raise HTTPException(
            status_code=404,
            detail=e.detail
        )
