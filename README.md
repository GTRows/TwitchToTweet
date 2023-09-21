# TwitchToTweet

TwitchToTweet is an automation bot that monitors changes in a Twitch stream's status, category, and title, and tweets
updates in real-time.

## Getting Started

Follow the steps below to run this project on your machine.

### Prerequisites

- Python 3.x
- Selenium
- Requests
- Firefox Web Browser (with Geckodriver)
- Python-decouple

### Installation

1. Clone or download the project.
2. Install the required Python libraries:
   ```
   pip install selenium requests python-decouple
   ```
3. Modify the `channels.json` file to add the Twitch channels you want to monitor.
4. Run GetTwitchAuthBearer.py to obtain your AUTH_BEARER token. Enter your Twitch CLIENT_ID and CLIENT_SECRET when
   prompted.
4. Add your `CLIENT_ID` and `AUTH_BEARER` for the Twitch API to the `.env` file.
5. On the first run, you will need to manually log in to your Twitter account. This is to save the cookies.

### Usage

- Run the `main.py` file to start the bot. It will begin monitoring Twitch streams and will automatically tweet any
  changes detected.
- You can manually test the Twitter automation functions by running the `Twitter.py` file.

## Contributing

This project is open source and contributions are welcome! Feel free to submit pull requests to add new features, fix
bugs, or improve documentation.

## License

This project is licensed under the MIT License. For more details, see the [LICENSE](LICENSE) file.

