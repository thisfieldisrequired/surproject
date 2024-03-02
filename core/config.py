from pathlib import Path
from pydantic_settings import BaseSettings

BASE_DIR = Path(__file__).parent.parent


class Settings(BaseSettings):
    db_url: str = 'sqlite+aiosqlite:///{BASE_DIR}/db.sqlie3'
    db_echo: bool = True


settings = Settings()