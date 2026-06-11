from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", case_sensitive=False
    )

    # Application
    app_name: str = "Learner API"
    debug: bool = False

    # Database
    # For Render, set DATABASE_URL environment variable to:
    # postgresql+psycopg://dinesh:YOUR_PASSWORD@dpg-d8li8ht8nd3s73e5aul0-a/language_database
    database_url: str = "postgresql+psycopg://user:password@localhost:5432/learner"

    # PostgreSQL connection details (can be used to construct DATABASE_URL)
    postgres_host: str = "localhost"
    postgres_port: int = 5432
    postgres_user: str = "postgres"
    postgres_password: str = ""
    postgres_db: str = "learner"

    @property
    def is_production(self) -> bool:
        """Determine if running in production environment"""
        return not self.debug


settings = Settings()
