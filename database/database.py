# import sqlite3
# from settings import Settings

# settings = Settings()

# def get_db_connection() -> sqlite3.Connection:            #  это функция подключения до sqlalchemy
#     return sqlite3.connect(settings.sqlite_db_name)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from settings import Settings

settings = Settings()


engine = create_engine(settings.db_url)
# engine = create_engine("sqlite:///pomodoro_db.sqlite")


Session = sessionmaker(engine)

def get_db_session() -> Session:
    return Session