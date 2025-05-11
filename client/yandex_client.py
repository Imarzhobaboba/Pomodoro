from dataclasses import dataclass
import requests
from settings import Settings
from schema import YandexUserData

@dataclass
class YandexClient:
    settings: Settings

    def get_user_info(self, code: str) -> YandexUserData:
        access_token = self._get_user_access_token(code=code)
        user_info = requests.get(
            'https://login.yandex.ru/info?format=json',
            headers={'Authorization': f"OAuth {access_token}"}
        )
        print(user_info.json())
        return YandexUserData(**user_info.json(), access_token=access_token)
        # return user_info.json()  # я это добавил сам
    def _get_user_access_token(self, code: str) -> str:
        data = {
            'code': code,
            'client_id': self.settings.YANDEX_CLIENT_ID,
            'client_secret': self.settings.YANDEX_SECRET_KEY,
            'grant_type': 'authorization_code',
        }
        headers = {
            'Content-Type': 'application/x-www-forn-urlencoded',
        }
        response = requests.post(self.settings.YANDEX_TOKEN_URL, 
                                 data=data,
                                 headers=headers)
        print(' ACCESS_TOKEN ЗДЕСЬ НАПИСАН. ВОТО ОН:   ', response.json()['access_token'])
        return response.json()['access_token']