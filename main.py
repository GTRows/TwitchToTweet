from Twitter import Twitter
from Twitch import Twitch
from Logger import Logger
import time
import datetime

log = Logger(__name__).get_logger()


def main():
    check_interval = 60
    print("Starting...")
    log.info("Starting...")
    twitter = Twitter()
    twitch = Twitch()

    while True:
        messages = twitch.check_channels()
        if len(messages) > 0:
            log.info(f"Found {len(messages)} messages to tweet!")
        else:
            log.info("No messages to tweet!")
        for msg in messages:
            log.info(f"Sending tweet: {msg}")
            twitter.send_tweet(msg)
        log.info(f"We're going to sleep for {check_interval} seconds...")
        time.sleep(check_interval)

    # This will never be printed
    log.error("Something went wrong!")


if __name__ == "__main__":
    main()
