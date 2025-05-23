from dataclasses import dataclass
from schema import UserLoginSchema
from repository.user import UserRepository
from service.auth import AuthService

@dataclass
class UserService:
    user_repository: UserRepository
    auth_service: AuthService

    async def create_user(
            self, 
            username: str, 
            password: str
    ) -> UserLoginSchema:
        user = await self.user_repository.create_user(
            username=username, 
            password=password,
            # access_token=access_token
        )
        access_token = self.auth_service.generate_access_token(user_id=user.id)
        return UserLoginSchema(
            user_id=user.id, 
            access_token=access_token)
    
    