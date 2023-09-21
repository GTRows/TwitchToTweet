import requests

CLIENT_ID = "YOUR_CLIENT_ID"
CLIENT_SECRET = "YOUR_CLIENT_SECRET"


def get_twitch_auth_bearer(client_id, client_secret):
    url = "https://id.twitch.tv/oauth2/token"
    params = {
        "client_id": client_id,
        "client_secret": client_secret,
        "grant_type": "client_credentials"
    }
    response = requests.post(url, params=params)
    data = response.json()
    return data.get("access_token", None)


auth_bearer = get_twitch_auth_bearer(CLIENT_ID, CLIENT_SECRET)
print(auth_bearer)
