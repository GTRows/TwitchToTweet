import Twitch
import Twitter
import time


def main():
    twitter = Twitter()
    twitch = Twitch()

    while True:
        messages = twitch.check_channels()
        for msg in messages:
            twitter.send_tweet(msg)
        time.sleep(60)


if __name__ == "__main__":
    main()
