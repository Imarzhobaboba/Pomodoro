from pydantic import BaseModel, Field, model_validator, ValidationInfo


class Task(BaseModel):

    # __tablename__ = 'tasks'         # этой строчки нет в курсе. Я добавил ее сам. Надо проверить, нужна ли она

    id: int | None = None
    name: str | None = None
    pomodoro_count: int | None = None
    category_id: int
    user_id: int

    class Config:
        from_attributes = True

    @model_validator(mode="after")
    def check_nameorcount(self):
        if self.name is None and self.pomodoro_count is None:
            raise ValueError('name or pomodoro_count must be provided')
        print(self)
        return(self)


class TaskCreateSchema(BaseModel):
    name: str | None = None
    pomodoro_count: int | None = None
    category_id: int