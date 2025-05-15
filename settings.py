from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_HOST: str = 'localhost'
    DB_PORT: int = 5431
    DB_USER: str = 'docker_postgres'
    DB_PASSWORD: str = 'docker_postgres'
    DB_DRIVER: str = 'postgresql+psycopg2'
    DB_NAME: str = 'docker_postgres'
    CACHE_HOST: str = 'localhost'
    CACHE_PORT: int = 6378
    CACHE_DB: int = 0
    JWT_SECRET_KEY: str = 'secret_key'
    JWT_ENCODE_ALGORITHM: str = 'HS256'
    GOOGLE_CLIENT_ID: str = ''
    GOOGLE_SECRET_KEY: str = ''   # это я тоже сам добавил
    GOOGLE_REDIRECT_URI: str = 'http://localhost:8000/api/auth/google/'   # хотя я хз. я сам это вставил.   P.S. оно сработало. оставляю    Теперь я убрал /api перед /auth
    GOOGLE_TOKEN_URL: str = ''
    # GOOGLE_TOKEN_URL: str = ''   # это чел из комментов написал
    # GOOGLE_TOKEN_URI: str = 'http://localhost:8000/api/auth/google/'
    YANDEX_TOKEN_ID: str = ''
    YANDEX_CLIENT_ID: str = ''
    YANDEX_SECRET_KEY: str = ''
    YANDEX_REDIRECT_URI: str = ''
    YANDEX_REDIRECT_KEY: str = 'http://localhost:8000/api/auth/yandex'
    YANDEX_TOKEN_URL: str = 'https://oauth.yandex.ru/token'


    @property
    def db_url(self):
        return f"{self.DB_DRIVER}://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    @property
    def google_redirect_url(self) -> str:
        return f'https://accounts.google.com/o/oauth2/auth?response_type=code&client_id={self.GOOGLE_CLIENT_ID}&redirect_uri={self.GOOGLE_REDIRECT_URI}&scope=openid%20profile%20email&access_type=offline'
    
    @property
    def yandex_redirect_url(self) -> str:
        return f'https://oauth.yandex.ru/authorize?response_type=code&client_id={self.YANDEX_CLIENT_ID}&redirect_uri={self.YANDEX_REDIRECT_URI}'