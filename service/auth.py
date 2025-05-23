from dataclasses import dataclass
from jose import jwt
from jose.exceptions import JWTError
import datetime
from datetime import timedelta
from database.models import UserProfile
from repository import UserRepository
from exception import TokenExpired, TokenNotCorrect, UserNotFoundException, UserNotCorrectPasswordException
from schema import UserLoginSchema, UserCreateSchema
from settings import Settings
from client import GoogleClient, YandexClient


@dataclass
class AuthService:
    user_repository: UserRepository
    settings: Settings
    google_client: GoogleClient
    yandex_client: YandexClient
    

    async def google_auth(self, code: str):
        user_data = await self.google_client.get_user_info(code=code)

        if user := await self.user_repository.get_google_user_by_email(email=user_data.email):
            access_token = self.generate_access_token(user_id=user.id)
            print('        user_login      ')
            return UserLoginSchema(user_id=user.id,
                                access_token=access_token)    
        # между create_user_data и UserLoginSchema я убрал await и все заработало
        create_user_data = UserCreateSchema(
            google_access_token=user_data.access_token,
            email=user_data.email,
            name=user_data.name,
        )
        # print('   USER_DATA ЗДЕСЬ НАПИСАНА:    ',user_data)
        created_user = await self.user_repository.create_user(create_user_data)
        access_token = self.generate_access_token(user_id=created_user.id)
        # print('          user_create        ')
        return UserLoginSchema(user_id=created_user.id,
                                access_token=access_token)
    
    async def yandex_auth(self, code: str):
        user_data = await self.yandex_client.get_user_info(code=code)

        if user := await self.user_repository.get_google_user_by_email(
            email=user_data.default_email):
            access_token = self.generate_access_token(user_id=user.id)
            return UserLoginSchema(user_id=user.id, access_token=access_token)
        created_user_data = UserCreateSchema(
            yandex_access_token=user_data.access_token,
            email=user_data.default_email,
            name=user_data.name,
        )
        created_user = await self.user_repository.create_user(created_user_data)
        access_token = self.generate_access_token(user_id=created_user.id)
        # print('       user data      ',user_data.json())
        # print('       created user      ',created_user.json())
        return UserLoginSchema(user_id=created_user.id, access_token=access_token)

    def get_google_redirect_url(self) -> str:
        return self.settings.google_redirect_url
    

    def get_yandex_redirect_url(self) -> str:
        return self.settings.yandex_redirect_url
    
    def get_yandex_auth(self, code: str):
        print(code)


    async def login(self, username: str, password: str) -> UserLoginSchema:
        user = await self.user_repository.get_user_by_username(username)
        self._validate_auth_user(user, password)
        access_token = self.generate_access_token(user_id=user.id)
        
        return UserLoginSchema(
            user_id=user.id, 
            access_token=access_token
        )
    
    @staticmethod      # staticmethod это метод, который не принимает себя (self)
    def _validate_auth_user(user: UserProfile, 
                            password: str
    ):
        if not user:
            raise UserNotFoundException
        if user.password != password:
            raise UserNotCorrectPasswordException
        
    def generate_access_token(self, user_id: int) -> str:
        expires_date_unix = (datetime.datetime.utcnow() + timedelta(days=7)).timestamp()
        token = jwt.encode(
            {'user_id': user_id, 'expire': expires_date_unix}, 
            self.settings.JWT_SECRET_KEY, 
            algorithm=self.settings.JWT_ENCODE_ALGORITHM)
        return token
    
    def get_user_id_from_access_token(self, access_token: str) -> int:
        try:
            payload = jwt.decode(access_token, self.settings.JWT_SECRET_KEY, algorithms=[self.settings.JWT_ENCODE_ALGORITHM])
        except JWTError:
            raise TokenNotCorrect
        
        if payload['expire'] < datetime.datetime.utcnow().timestamp():
            raise TokenExpired
        
        return payload['user_id']
    
    