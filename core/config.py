from pathlib import Path
from pydantic_settings import BaseSettings
from pydantic import BaseModel

BASE_DIR = Path(__file__).parent.parent
DB_PATH = BASE_DIR / "db.sqlite3"


class DbSettings(BaseModel):
    url: str = f"sqlite+aiosqlite:///{DB_PATH}"
    echo: bool = True


class AuthJWT(BaseModel):
    private_key_path: Path = BASE_DIR / "certs" / "jwt-private.pem"
    public_key_path: Path = BASE_DIR / "certs" / "jwt-public.pem"
    algorithm: str = "RS256"


class Settings(BaseSettings):
    api_v1_prefix: str = "/api/v1"
    db: DbSettings = DbSettings()
    auth_jwt: AuthJWT = AuthJWT()


settings = Settings()
