from dotenv import load_dotenv
from pydantic import BaseSettings, SecretStr


class BotConfig(BaseSettings):
    db_host: str
    db_port: int
    db_user: str
    db_pass: SecretStr
    db_name: str

    class Config:
        env_prefix = "AIR_BOT_ADMIN_"

    def get_mysql_uri(self) -> str:
        uri_template = "mysql+asyncmy://{user}:{password}@{host}:{port}/{db_name}"
        return uri_template.format(
            user=self.db_user,
            password=self.db_pass.get_secret_value(),
            host=self.db_host,
            port=self.db_port,
            db_name=self.db_name,
        )


load_dotenv()
config = BotConfig()