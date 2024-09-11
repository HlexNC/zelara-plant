from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    kindwise_api_key: str
    mongo_url: str
    environment: str = "development"

    class Config:
        env_file = ".env"

# Initialize settings
settings = Settings()
