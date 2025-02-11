from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    aws_region: str
    dynamodb_table: str
    aws_access_key_id: str
    aws_secret_access_key: str
    aws_session_token: str

    exams_service_url: str
    appointments_service_url: str
    prescriptions_service_url: str

    class Config:
        env_file = ".env"

settings = Settings()