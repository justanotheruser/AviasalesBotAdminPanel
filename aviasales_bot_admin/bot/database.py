from typing import AsyncIterator

from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession

from aviasales_bot_admin.config import config

engine = create_async_engine(
    config.get_mysql_uri(), echo=True, future=True, pool_pre_ping=True
)
SessionLocal = sessionmaker(
    engine, class_=AsyncSession, autocommit=False, autoflush=False
)  # type: ignore[call-overload]


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)


async def get_db() -> AsyncIterator[AsyncSession]:
    async with SessionLocal() as session:
        yield session
