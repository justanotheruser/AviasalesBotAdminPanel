from sqlmodel import Field, SQLModel, create_engine
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from aviasales_bot_admin.config import config


class User(SQLModel, table=True):
    user_id: int | None = Field(default=None, primary_key=True)


engine = create_async_engine(config.get_mysql_uri(), echo=True, future=True, pool_pre_ping=True)


"""
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)


async def get_session() -> AsyncSession:
    async_session = sessionmaker(
        engine, class_=AsyncSession, expire_on_commit=False
    )
    async with async_session() as session:
        yield session
"""