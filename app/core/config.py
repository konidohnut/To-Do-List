from dotenv import load_dotenv
from pydantic.v1 import BaseSettings
import os

load_dotenv()


class Settings(BaseSettings):
    fast_api_port: int = os.getenv('FAST_API_PORT')
    fast_api_host: str = os.getenv('FAST_API_HOST')

    postgres_user: str = os.getenv('POSTGRES_USER')
    postgres_password: str = os.getenv('POSTGRES_PASSWORD')
    postgres_db: str = os.getenv('POSTGRES_DB')

    postgres_host: str = os.getenv('POSTGRES_HOST')
    postgres_port: int = os.getenv('POSTGRES_PORT')

    @property
    def postgresql_url(self) -> str:
        return f"postgresql+asyncpg://{self.postgres_user}:{self.postgres_password}@{self.postgres_host}:{self.postgres_port}/{self.postgres_db}"


settings = Settings()

