import pathlib
from typing import Dict

import yaml
from pydantic import BaseSettings, SecretStr


class BotConfig(BaseSettings):
    db_host: str
    db_port: int
    db_user: str
    db_pass: SecretStr
    db_name: str

    def get_mysql_uri(self) -> str:
        uri_template = "mysql+asyncmy://{user}:{password}@{host}:{port}/{db_name}"
        return uri_template.format(
            user=self.db_user,
            password=self.db_pass.get_secret_value(),
            host=self.db_host,
            port=self.db_port,
            db_name=self.db_name,
        )


class Config(BaseSettings):
    bots: Dict[str, BotConfig]


def load_config(config_path: pathlib.Path) -> Config:
    with open(config_path, 'r') as file:
        data = yaml.load(file, Loader=yaml.SafeLoader)
    return Config(**data)


def default_config_path() -> pathlib.Path:
    return pathlib.Path(__file__).parent.parent.resolve() / 'config.yaml'


config = load_config(default_config_path())
