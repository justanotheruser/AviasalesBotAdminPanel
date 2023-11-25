from fastapi import Depends, FastAPI

from aviasales_bot_admin.bot.database import DBManager
from aviasales_bot_admin.bot.views import create_views
from aviasales_bot_admin.config import BotConfig


class BotInfoAPI:
    def __init__(self, bot_name: str, config: BotConfig):
        self.bot_name = bot_name
        self.app = FastAPI()
        self.db_manager = DBManager(config)
        self.db = Depends(self.db_manager.get_db)
        create_views(self.app, self.bot_name, self.db)
