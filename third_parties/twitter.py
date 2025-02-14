import os
from dotenv import load_dotenv
import tweepy
import requests

load_dotenv()


twitter_client = tweepy.Client(
    bearer_token=os.environ["TWITTER_BEARER_TOKEN"],
    consumer_key=os.environ["TWITTER_API_KEY"],
    consumer_secret=os.environ["TWITTER_API_KEY_SECRET"],
    access_token=os.environ["TWITTER_ACCESS_TOKEN"],
    access_token_secret=os.environ["TWITTER_ACCESS_TOKEN_SECRET"],
)


def scrape_user_tweets(username, num_tweets=5):
    """
    Scrapes a Twitter user's original tweets (i.e., not retweets or replies) and returns them as a list of dictionaries.
    Each dictionary has three fields: "time_posted" (relative to now), "text", and "id".
    """
    user_id = twitter_client.get_user(username=username).data.id
    tweets = twitter_client.get_users_tweets(
        id=user_id, max_results=num_tweets, exclude=["retweets", "replies"]
    )
    print(tweets.data)
    print('------------------------------------------------------------')
    tweet_list = []
    for tweet in tweets.data:
        tweet_dict = {}
        tweet_dict["id"] = tweet["id"]
        tweet_dict["text"] = tweet["text"]
        tweet_list.append(tweet_dict)

    return tweet_list


def scrape_user_tweets_mock(username="shakhotai", num_tweets=5):
    """
    Scrapes pre made Edens's Github Gist file of tweets and returns them as a list of dictionaries.
    Each dictionary has three fields: "time_posted" (relative to now), "text", and "url".
    https://twitter.com/EdenEmarco177
    """
    #TWITTER_GIST = "https://gist.githubusercontent.com/emarco177/827323bb599553d0f0e662da07b9ff68/raw/57bf38cf8acce0c87e060f9bb51f6ab72098fbd6/eden-marco-twitter.json"
    TWITTER_GIST = "https://gist.githubusercontent.com/shakhot/a597426348275f7f57c58cc63763375c/raw/cb58c5ac7a1ed5b3fbca2ef97230649867b76d2c/shakhotai-tweet.json"
    tweets = requests.get(TWITTER_GIST, timeout=5).json()

    tweet_list = []
    for tweet in tweets:

        tweet_dict = {}
        tweet_dict["id"] = tweet["id"]
        tweet_dict["text"] = tweet["text"]
        tweet_list.append(tweet_dict)

    return tweet_list


if __name__ == "__main__":

    #tweets = scrape_user_tweets_mock(username="EdenEmarco177")
    tweets = scrape_user_tweets_mock(username="shakhotai")    
    print(tweets)