from typing import Sequence

from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from aviasales_bot_admin.bot.models import FlightDirection


class FlightDirectionsRepo:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_list(self) -> Sequence[FlightDirection]:
        query = select(FlightDirection)
        result = await self.session.exec(query)
        return result.all()
