from selenium import webdriver
import pickle
import time
from selenium.common.exceptions import NoSuchElementException


class Twitter:

    def __init__(self):
        options = webdriver.FirefoxOptions()
        options.headless = True

        self.driver = webdriver.Firefox(options=options)
        self.cookie_file = "twitter_cookies.pkl"

    def save_cookies(self):
        cookies = self.driver.get_cookies()
        with open(self.cookie_file, "wb") as file:
            pickle.dump(cookies, file)

    def load_cookies(self):
        with open(self.cookie_file, "rb") as file:
            cookies = pickle.load(file)
            for cookie in cookies:
                self.driver.add_cookie(cookie)

    def login(self):
        self.driver.get("https://twitter.com/login")
        input("Giriş yaptıktan sonra enter tuşuna basınız...")
        self.save_cookies()

    def send_tweet(self, message):
        self.driver.get("https://twitter.com")
        self.load_cookies()
        self.driver.refresh()

        tweet_button = self.find_element_with_wait("xpath", "//a[@data-testid='SideNav_NewTweet_Button']")
        tweet_button.click()

        tweet_textbox = self.find_element_with_wait("xpath", "//div[@role='textbox']")
        tweet_textbox.send_keys(message)

        send_tweet_button = self.find_element_with_wait("xpath", "//div[@data-testid='tweetButton']")
        send_tweet_button.click()

        time.sleep(4)
        print("Tweet sent!")

    def find_element_with_wait(self, method, value, timeout=10):
        for _ in range(timeout):
            try:
                return self.driver.find_element(method, value)
            except NoSuchElementException:
                time.sleep(1)
        raise NoSuchElementException(f"Element ({method}, {value}) couldn't be found after {timeout} seconds!")

    def close(self):
        self.driver.close()


if __name__ == "__main__":
    twitter = Twitter()
    action = input("Login or Send Tweet? (login/send): ")

    if action == "login":
        twitter.login()
    elif action == "send":
        message = input("Enter your tweet: ")
        twitter.send_tweet(message)

    twitter.close()
