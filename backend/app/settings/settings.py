from pydantic_settings import BaseSettings
from yarl import URL
class Settings(BaseSettings):
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str

    API_BASE_PORT: int

    JWT_ALGORITHM: str
    JWT_SECRET_KEY: str
    JWT_ACCESS_TOKEN_LIFETIME_HOURS: int
    
    class Config:
        env_file = ".env"

    @property
    def db_url(self) -> URL:
        
        url = URL.build (
            scheme="postgresql+asyncpg",
            host=self.POSTGRES_HOST,
            port=self.POSTGRES_PORT,
            user=self.POSTGRES_USER,
            password=self.POSTGRES_PASSWORD,
            path=f"/{self.POSTGRES_DB}"
        )
        print(url)
        return url
    
settings: Settings = Settings()