# import sqlite3
# from settings import Settings

# settings = Settings()

# def get_db_connection() -> sqlite3.Connection:            #  это функция подключения до sqlalchemy
#     return sqlite3.connect(settings.sqlite_db_name)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine("postgresql+psycopg2://docker_postgres:docker_postgres@localhost:5431/docker_postgres")
# engine = create_engine("sqlite:///pomodoro_db.sqlite")


Session = sessionmaker(engine)

def get_db_session() -> Session:
    return Session