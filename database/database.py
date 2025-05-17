# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker

# from settings import Settings

# settings = Settings()


# engine = create_engine(settings.db_url)


# Session = sessionmaker(engine)

# def get_db_session() -> Session:
#     return Session

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession


from settings import Settings

settings = Settings()

engine = create_async_engine(
    url=Settings().db_url,
    future=True,
    echo=True,
    pool_pre_ping=True
)


AsyncSessionFactory =  async_sessionmaker(
    engine,
    autoflush=False,
    expire_on_commit=False
)


async def get_db_session() -> AsyncSession:
    async with AsyncSessionFactory() as session:
        yield session