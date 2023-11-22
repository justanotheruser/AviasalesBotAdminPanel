from typing import Sequence

from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from aviasales_bot_admin.bot.models import User


class UsersRepo:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_list(self) -> Sequence[User]:
        query = select(User)
        result = await self.session.exec(query)
        return result.all()
