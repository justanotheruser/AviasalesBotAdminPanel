from typing import AsyncIterator

from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel.ext.asyncio.session import AsyncSession

from aviasales_bot_admin.config import BotConfig


class DBManager:
    def __init__(self, config: BotConfig):
        self._engine = create_async_engine(
            config.get_mysql_uri(), echo=True, future=True, pool_pre_ping=True
        )
        self.sessionmaker = sessionmaker(
            self._engine, class_=AsyncSession, autocommit=False, autoflush=False
        )  # type: ignore[call-overload]

    async def get_db(self) -> AsyncIterator[AsyncSession]:
        async with self.sessionmaker() as session:
            yield session
