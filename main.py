from Twitter import Twitter
from Twitch import Twitch
import time
import datetime


def main():
    print("Starting...")
    twitter = Twitter()
    twitch = Twitch()

    while True:
        messages = twitch.check_channels()
        print(f"Found {len(messages)} messages to tweet!")
        for msg in messages:
            print(f"Sending tweet: {msg}")
            twitter.send_tweet(msg)
        print(f"Checked at {datetime.datetime.now()}")
        time.sleep(60)

    # This will never be printed,
    print("Done!")


if __name__ == "__main__":
    main()
