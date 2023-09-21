import requests


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


if __name__ == "__main__":
    CLIENT_ID = "YOUR_CLIENT_ID"
    CLIENT_SECRET = "YOUR_CLIENT_SECRET"

    # If you don't want to hardcode your client ID and secret, you can enter them here
    if CLIENT_ID == "YOUR_CLIENT_ID":
        CLIENT_ID = input("Enter your client ID: ")
        CLIENT_SECRET = input("Enter your client secret: ")

    auth_bearer = get_twitch_auth_bearer(CLIENT_ID, CLIENT_SECRET)
    print(f"Your auth bearer is: {auth_bearer}")
