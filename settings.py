from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # GOOGLE_TOKEN_ID: str = "hhf43u3hqto438hgo784u"
    sqlite_db_name: str = 'pomodoro_db.sqlite'