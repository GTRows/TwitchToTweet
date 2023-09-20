import requests
import json
from decouple import config


class Twitch:

    def __init__(self):
        self.CLIENT_ID = config('CLIENT_ID')
        self.AUTH_BEARER = config('AUTH_BEARER')
        with open("channels.json", "r") as file:
            self.data = json.load(file)

    def is_channel_live(self, channel_name):
        url = f'https://api.twitch.tv/helix/streams?user_login={channel_name}'
        headers = {
            'Client-ID': self.CLIENT_ID,
            'Authorization': f'Bearer {self.AUTH_BEARER}'
        }
        response = requests.get(url, headers=headers)
        data = response.json()

        try:
            if len(data['data']) > 0:
                return data['data'][0]
        except KeyError:
            print(f"Unexpected response structure from API for channel: {channel_name}. Response: {data}")
            return None
        return None

    def check_channels(self):
        messages_to_tweet = []

        for channel in self.data['channels']:
            twitch_data = self.is_channel_live(channel['name'])
            if twitch_data:
                if not channel['isLive'] and channel['notify']['live']:
                    message = f"{channel['name']} has just gone live!"
                    messages_to_tweet.append(message)
                    channel['isLive'] = True

                if channel['lastTitle'] != twitch_data['title'] and channel['notify']['titleChange']:
                    message = f"{channel['name']} has changed the title to {twitch_data['title']}!"
                    messages_to_tweet.append(message)
                    channel['lastTitle'] = twitch_data['title']

                if channel['lastCategory'] != twitch_data['game_name'] and channel['notify']['categoryChange']:
                    message = f"{channel['name']} is now streaming {twitch_data['game_name']}!"
                    messages_to_tweet.append(message)
                    channel['lastCategory'] = twitch_data['game_name']
            else:
                channel['isLive'] = False

        # Save the updated data back to the JSON file
        with open("channels.json", "w") as file:
            json.dump(self.data, file, indent=4)

        return messages_to_tweet


if __name__ == "__main__":
    twitch = Twitch()
    twitch.check_channels()
