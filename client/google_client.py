from dataclasses import dataclass
import httpx
from settings import Settings
from schema import GoogleUserData

@dataclass
class GoogleClient:
    settings: Settings
    # async_client: httpx.AsyncClient

    async def get_user_info(self, code: str) -> GoogleUserData:
        async with httpx.AsyncClient() as client:
            access_token = await self._get_user_access_token(code=code, client=client)
            user_info = await client.get(
                    'https://www.googleapis.com/oauth2/v1/userinfo',
                    headers={'Authorization': f"Bearer {access_token}"}
                )
            return GoogleUserData(**user_info.json(), access_token=access_token)
            # return user_info.json()  # я это добавил сам
    async def _get_user_access_token(self, code: str, client: httpx.AsyncClient) -> str:        
        # async with self.async_client as client:
        response = await client.post(
            url=self.settings.GOOGLE_TOKEN_URL, 
            data={
                'code': code,
                'client_id': self.settings.GOOGLE_CLIENT_ID,
                'client_secret': self.settings.GOOGLE_SECRET_KEY,
                'redirect_uri': self.settings.GOOGLE_REDIRECT_URI,
                'grant_type': 'authorization_code',
            }
        )
        # print(' ACCESS_TOKEN ЗДЕСЬ НАПИСАН. ВОТО ОН:   ', response.json()['access_token'])
        return response.json()['access_token']