from typing import Sequence

from sqlalchemy.sql import func
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from aviasales_bot_admin.bot.models import User, UserDirection


class UsersRepo:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_list(self) -> Sequence[User]:
        query = select(User)
        result = await self.session.exec(query)
        return result.all()

    async def get_full_info_list(self):
        query = select(
            User.user_id, func.count(UserDirection.direction_id).label('n_directions')
        )
        query = query.join(UserDirection, isouter=True).group_by(User.user_id)
        result = await self.session.exec(query)
        return result.all()
