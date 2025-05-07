from sqlalchemy.orm import Mapped, mapped_column, declarative_base, DeclarativeBase, declared_attr

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


class Categories(Base):
    __tablename__="categories"

    id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[str]
    name: Mapped[str]


class UserProfile(Base):
    __tablename__ = 'userprofile'
    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    username: Mapped[str] = mapped_column(nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    access_token: Mapped[str] = mapped_column(nullable=False)