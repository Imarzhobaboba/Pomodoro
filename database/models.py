from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, declared_attr
from typing import Optional

class Base(DeclarativeBase):
    id: any
    __name__: str

    __allow_unmapped__ = str = True

    @declared_attr
    def __tablename__(self) -> str:
        return self.__name__.lower()



# Base = declarative_base()

class Tasks(Base):
    __tablename__="tasks"           # ЭТА КУРВА ДОЛЖНА БЫТЬ С МАЛЕНЬКОЙ БУКВЫ

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    pomodoro_count: Mapped[int]
    category_id: Mapped[int]
    user_id: Mapped[int] = mapped_column(ForeignKey('userprofile.id'), nullable=False)


class Categories(Base):
    __tablename__="categories"

    id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[str]
    name: Mapped[str]


class UserProfile(Base):
    __tablename__ = 'userprofile'
    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    username: Mapped[str] = mapped_column(nullable=True)
    password: Mapped[str] = mapped_column(nullable=True)
    google_access_token: Mapped[Optional[str]]
    email: Mapped[Optional[str]]
    name: Mapped[Optional[str]]