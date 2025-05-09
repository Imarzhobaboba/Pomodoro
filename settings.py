from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # GOOGLE_TOKEN_ID: str = "hhf43u3hqto438hgo784u"
    # sqlite_db_name: str = 'pomodoro_db.sqlite'
    DB_HOST: str = 'localhost'
    DB_PORT: int = 5431
    DB_USER: str = 'docker_postgres'
    DB_PASSWORD: str = 'docker_postgres'
    DB_DRIVER: str = 'postgresql+psycopg2'
    DB_NAME: str = 'docker_postgres'
    CACHE_HOST: str = 'localhost'
    CACHE_PORT: int = 6378
    CACHE_DB: int = 0
    JWT_SECRET_KEY: str = 'secret_key'
    JWT_ENCODE_ALGORITHM: str = 'HS256'

    @property
    def db_url(self):
        return f"{self.DB_DRIVER}://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
