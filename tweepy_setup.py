import tweepy
import os
import time
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Use environment variables for security
api_key = os.getenv("TWITTER_API_KEY")
api_secret = os.getenv("TWITTER_API_SECRET")
bearer_token = os.getenv("TWITTER_BEARER_TOKEN")
access_token = os.getenv("TWITTER_ACCESS_TOKEN")
access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

# Check if all required environment variables are set
if not all([api_key, api_secret, bearer_token, access_token, access_token_secret]):
    raise ValueError("Missing required environment variables. Please check your .env file.")

client = tweepy.Client(
    bearer_token, api_key, api_secret, access_token, access_token_secret
)

auth = tweepy.OAuth1UserHandler(
    api_key, api_secret, access_token, access_token_secret
)
api = tweepy.API(auth)

search_terms = ["nairobi kenya", "tech event", "software developers"]

class MyStream(tweepy.StreamingClient):
    def on_connect(self):
        print("Connected to Twitter Streaming API")

    def on_tweet(self, tweet):
        if tweet.referenced_tweets == None:
            print(tweet.text)

            time.sleep(0.2)

stream = MyStream(bearer_token)

for term in search_terms:
    stream.add_rules(tweepy.StreamRule(term))

stream.filter(tweet_fields=["referenced_tweets"])

recent_tweets = client.search_recent_tweets(query="developers event", max_results=10)
for tweet in recent_tweets.data:
    print(tweet.text)


# Liking a tweet
tweet_id = "1234567890123456789"  # Replace with the actual tweet ID
# retweeting a tweet
client.retweet(tweet_id)
client.create_tweet(in_reply_to_tweet_id=tweet_id, text="This is a reply to the tweet." )

try:
    response = client.create_tweet(
        text="Hello, world! This is a tweet created using Tweepy."
    )
    print(f"Tweet created successfully! Tweet ID: {response.data['id']}")
except Exception as e:
    print(f"Error creating tweet: {e}")

