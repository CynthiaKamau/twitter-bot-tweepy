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

client = tweepy.Client(bearer_token=bearer_token)

client_with_auth = tweepy.Client(
    bearer_token, api_key, api_secret, access_token, access_token_secret
)

def find_and_quote_tweets():
    """
    Alternative to retweeting: Quote tweets or create inspired content
    This works with free tier for posting
    """
    search_terms = ["nairobi tech", "python programming", "web development"]
    
    try:
        # Search for tweets (free tier allows limited search)
        query = " OR ".join(search_terms)
        tweets = client.search_recent_tweets(
            query=query,
            max_results=10,
            tweet_fields=["author_id", "created_at", "public_metrics"]
        )
        
        if tweets.data:
            for tweet in tweets.data[:3]:  # Process only first 3 to avoid spam
                # Instead of retweeting, create quote-style content
                quote_text = f"Interesting perspective on tech: {tweet.text[:100]}..."
                
                # Post as a new tweet (this works on free tier)
                try:
                    response = client_with_auth.create_tweet(text=quote_text)
                    print(f"Posted quote tweet: {response.data['id']}")
                    time.sleep(5)  # Avoid rate limits
                except Exception as e:
                    print(f"Failed to post tweet: {e}")
                    
    except tweepy.Forbidden as e:
        print(f"Search access denied: {e}")
    except Exception as e:
        print(f"Error: {e}")

def create_curated_content():
    """
    Alternative approach: Create original content inspired by trending topics
    """
    search_terms = ["AI trends", "startup news", "tech events nairobi"]
    
    try:
        for term in search_terms:
            tweets = client.search_recent_tweets(
                query=term,
                max_results=5
            )
            
            if tweets.data:
                # Analyze trending topics and create original content
                tweet_texts = [tweet.text for tweet in tweets.data]
                
                # Create summary or commentary (manual example)
                summary_tweet = f"Seeing lots of discussion about {term} today. Here's what I'm thinking... #TechTrends"
                
                try:
                    response = client_with_auth.create_tweet(text=summary_tweet)
                    print(f"Posted curated content: {response.data['id']}")
                    time.sleep(10)  # Longer delay between posts
                except Exception as e:
                    print(f"Failed to post: {e}")
                    
    except Exception as e:
        print(f"Error: {e}")

def simple_posting_bot():
    """
    Simple bot that posts original content about specific topics
    """
    topics = [
        "Just learned something new about Python! #coding #python",
        "Excited about the tech scene in Nairobi! #NairobiTech",
        "Working on a new project today. #developer #coding"
    ]
    
    for topic in topics:
        try:
            response = client_with_auth.create_tweet(text=topic)
            print(f"Posted: {response.data['id']}")
            time.sleep(30)  # Wait 30 seconds between posts
        except Exception as e:
            print(f"Failed to post: {e}")

# Example usage
if __name__ == "__main__":
    find_and_quote_tweets()
    create_curated_content()
    simple_posting_bot()
    print("Free tier Twitter automation alternatives:")
    print("1. Quote-style content")
    print("2. Curated original content")
    print("3. Simple posting bot")