# Twitter Bot with Tweepy

A Python-based Twitter bot that can interact with the Twitter API using Tweepy. This bot can create tweets, search for tweets, stream real-time tweets, like tweets, retweet, and reply to tweets.

## Features

- 🐦 Create and post tweets
- 🔍 Search for recent tweets
- 📡 Real-time tweet streaming
- ❤️ Like tweets
- 🔄 Retweet functionality
- 💬 Reply to tweets
- 🔐 Secure credential management with environment variables

## Prerequisites

- Python 3.7+
- Twitter Developer Account
- Twitter API v2 credentials (API Key, API Secret, Bearer Token, Access Token, Access Token Secret)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/twitter-bot-tweepy.git
cd twitter-bot-tweepy
```

2. Install required packages:
```bash
pip install tweepy==4.9.0 python-dotenv
```

3. Create a `.env` file in the project root and add your Twitter API credentials:
```
TWITTER_API_KEY=your_api_key_here
TWITTER_API_SECRET=your_api_secret_here
TWITTER_BEARER_TOKEN=your_bearer_token_here
TWITTER_ACCESS_TOKEN=your_access_token_here
TWITTER_ACCESS_TOKEN_SECRET=your_access_token_secret_here
```

## Usage

Run the bot:
```bash
python tweepy_setup.py
```

## Configuration

- Modify `search_terms` array to customize what topics the bot monitors
- Update tweet content in the `create_tweet()` function
- Adjust streaming filters in the `MyStream` class

## Project Structure

```
twitter-bot-tweepy/
├── tweepy_setup.py     # Main bot script
├── .env                # Environment variables (create this)
├── README.md           # This file
└── .gitignore          # Git ignore file
```

## Security Notes

- Never commit your `.env` file to version control
- Keep your API credentials secure and private
- Consider using Twitter's rate limiting guidelines

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License.

## Disclaimer

This bot is for educational purposes. Please comply with Twitter's Terms of Service and API usage policies.
