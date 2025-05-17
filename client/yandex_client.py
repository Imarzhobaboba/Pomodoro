from dataclasses import dataclass
import httpx
from settings import Settings
from schema import YandexUserData

@dataclass
class YandexClient:
    settings: Settings
    # async_client: httpx.AsyncClient

    async def get_user_info(self, code: str) -> YandexUserData:
        async with httpx.AsyncClient() as client:
            access_token = await self._get_user_access_token(code=code, client=client)
            user_info = await client.get(
                'https://login.yandex.ru/info?format=json',
                headers={'Authorization': f"OAuth {access_token}"}
            )
            # print(user_info.json())
        return YandexUserData(**user_info.json(), access_token=access_token)
        # return user_info.json()  # я это добавил сам
    async def _get_user_access_token(self, code: str, client: httpx.AsyncClient) -> str:
        # async with httpx.AsyncClient() as client:
        response = await client.post(self.settings.YANDEX_TOKEN_URL, 
            data={
                'code': code,
                'client_id': self.settings.YANDEX_CLIENT_ID,
                'client_secret': self.settings.YANDEX_SECRET_KEY,
                'grant_type': 'authorization_code',
            },
            headers={
                'Content-Type': 'application/x-www-forn-urlencoded',
            }
        )
        # print(' ACCESS_TOKEN ЗДЕСЬ НАПИСАН. ВОТО ОН:   ', response.json()['access_token'])
        return response.json()['access_token']