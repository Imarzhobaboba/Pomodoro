from typing import Annotated

from fastapi import APIRouter,status, Depends

# from fixtures import tasks as fixtures_tasks
from dependency import get_tasks_repository, get_tasks_cache_repository
from schema.task import Task
from repository import TaskRepository, TaskCache

# from database.database import get_db_connection
from database.database import get_db_session


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
        # result : list[Task] = []
        # cursor = get_db_session().cursor()
        # tasks = cursor.execute("select * from Tasks").fetchall()
        # # print(tasks)
        # for task in tasks:
        #     result.append(Task(
        #         id=task[0],
        #         name=task[1],
        #         pomodoro_count=task[2],
        #         category_id=task[3]
        #     ))
        return tasks_schema


@router.post(
        "/",
        response_model=Task
)
async def create_task(
    task: Task,
    task_repository: Annotated[TaskRepository, Depends(get_tasks_repository)]
):
    task_repository.create_task(task)
    # connection = get_db_session()
    # cursor = connection.cursor()
    # cursor.execute("insert into Tasks (name, pomodoro_count, category_id) values (?,?,?)", (task.name, task.pomodoro_count, task.category_id))
    # connection.commit()
    # connection.close()
    # # fixtures_tasks.append(task)
    return task



'''@router.put(
    "/{task_id}",
    response_model=Task
)
async def update_task(task_id: int, name: str):
    for task in fixtures_tasks:
        if task_id==task["id"]:
            task["name"]=name
            return task'''
        

# это патч до работы с sql
'''@router.patch(
    "/{task_id}",
    response_model=Task
)
async def update_task(task_id: int, name: str):
    for task in fixtures_tasks:
        if task_id==task["id"]:
            task["name"]=name
            return task'''

@router.patch(
    "/{task_id}",
    response_model=Task
)
async def update_task(
    task_id: int, 
    name: str,
    task_repository: Annotated[TaskRepository, Depends(get_tasks_repository)]
):
    # connection = get_db_connection()
    # cursor = connection.cursor()
    # cursor.execute("update Tasks set name =? where id =?", (name, task_id))
    # connection.commit()
    # task = cursor.execute("select * from Tasks where id =?", f"{task_id}").fetchall()[0]
    # connection.close()
    return task_repository.update_task_name(task_id, name)
    
    # return Task(
    #     id=task[0],
    #     name=task[1],
    #     pomodoro_count=task[2],
    #     category_id=task[3])


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(task_id:int):
    connection = get_db_session()
    cursor = connection.cursor()
    cursor.execute("delete from Tasks where id =?", (task_id,))
    connection.commit()
    connection.close()
    return {"message": f"task with {task_id} id is deleted"}


# удаление до sql
'''@router.delete("/{task_id}")
async def delete_task(task_id:int):
    for index, task in enumerate(fixtures_tasks):
        if task["id"] == task_id:
            del fixtures_tasks[index]
            return {"message": f"task with {task_id} id is deleted"}'''
