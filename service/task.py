from dataclasses import dataclass
from repository import TaskRepository, TaskCache
from schema.task import Task, TaskCreateSchema
from exception import TaskNotFound
from fastapi import HTTPException, status


@dataclass
class TaskService:
    task_repository: TaskRepository
    task_cache: TaskCache

    async def get_tasks(self):
        if cache_task := await self.task_cache.get_tasks():
            return cache_task
        else:
            tasks = await self.task_repository.get_tasks()
            tasks_schema = [Task.model_validate(task) for task in tasks]

            try:        # try except raise я написал сам, потому что выызывается ошибка , если в бд нет тасков
                await self.task_cache.set_tasks(tasks_schema)
                return tasks_schema
            except Exception as e:
                raise HTTPException(
                    status_code=status.HTTP_204_NO_CONTENT,
                    detail='You have not created any tasks yet'
                )
            
        
    async def create_task(self, body: TaskCreateSchema, user_id: int) -> Task:
        task_id = await self.task_repository.create_task(body, user_id)
        task = await self.task_repository.get_task(task_id)
        return Task.model_validate(task)
    
    async def update_task_name(self, task_id: int, name: str, user_id: int) -> Task:
        task = await self.task_repository.get_user_task(user_id=user_id, task_id=task_id)
        if not task:
            raise TaskNotFound
        task = await self.task_repository.update_task_name(task_id=task_id, name=name)
        return Task.model_validate(task)
    
    async def delete_task(self, task_id: int, user_id: int) -> None:
        task = await self.task_repository.get_user_task(user_id=user_id, task_id=task_id)
        if not task:
            raise TaskNotFound
        await self.task_repository.delete_task(task_id=task_id, user_id=user_id)