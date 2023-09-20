import requests
from decouple import config


class Twitch:

    def __init__(self):
        self.CLIENT_ID = config('CLIENT_ID')
        self.AUTH_BEARER = config('AUTH_BEARER')
        self.CHANNEL_NAME = 'jahrein'

    def is_channel_live(self, channel_name=None):
        if not channel_name:
            channel_name = self.CHANNEL_NAME

        # Twitch API endpoint
        url = f'https://api.twitch.tv/helix/streams?user_login={channel_name}'

        headers = {
            'Client-ID': self.CLIENT_ID,
            'Authorization': f'Bearer {self.AUTH_BEARER}'
        }

        response = requests.get(url, headers=headers)
        data = response.json()

        try:
            return len(data['data']) > 0
        except KeyError as e:
            print("KeyError:", e)
            return False


if __name__ == "__main__":
    twitch = Twitch()
    if twitch.is_channel_live():
        print(f"{twitch.CHANNEL_NAME} is live!")
    else:
        print(f"{twitch.CHANNEL_NAME} is not live.")
