
from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase


DATABASE_URL = "postgresql+asyncpg://f1_user:f1_password@localhost:5433/f1_database"


engine = create_async_engine(DATABASE_URL, echo=True)

asyncSessionMaker = async_sessionmaker(engine, class_= AsyncSession, expire_on_commit=False)

class Base(DeclarativeBase):
    pass

# create function to essentially creat a session for each request
async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with asyncSessionMaker() as session:
        try:
            yield session
        except Exception as e:
            await session.rollback()
            raise
        finally:
            await session.close()
