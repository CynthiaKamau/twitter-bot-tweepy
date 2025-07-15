def simple_search():
    """One-time search that works with free tier"""
    try:
        query = " OR ".join(search_terms)
        tweets = client.search_recent_tweets(
            query=query,
            max_results=10
        )
        
        if tweets.data:
            for tweet in tweets.data:
                print(tweet.text)
                print("-" * 50)
        else:
            print("No tweets found")
            
    except tweepy.Forbidden as e:
        print(f"Access denied: {e}")
    except Exception as e:
        print(f"Error: {e}")

simple_search()