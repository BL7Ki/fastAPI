from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):  # tipo o basemodels
    model_config = SettingsConfigDict(
        env_file='.env', env_file_encoding='utf-8'  # fala onde ta o arquivo de configuracoes e qual o encoding dele
    )

    DATABASE_URL: str
