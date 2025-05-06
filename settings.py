from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # GOOGLE_TOKEN_ID: str = "hhf43u3hqto438hgo784u"
    # sqlite_db_name: str = 'pomodoro_db.sqlite'
    DB_HOST: str = 'localhost'
    DB_PORT: int = 5431
    DB_USER: str = 'docker_postgres'
    DB_PASSWORD: str = 'docker_postgres'
    DB_NAME: str = 'docker_postgres'
    CACHE_HOST: str = 'localhost'
    CACHE_PORT: int = 6378
    CACHE_DB: int = 0