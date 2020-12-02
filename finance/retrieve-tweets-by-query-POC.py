import os
import secrets
import tweepy as tw
import pandas as pd


auth = tw.OAuthHandler(secrets.twitter_consumer_key, secrets.twitter_consumer_secret)
api = tw.API(auth, wait_on_rate_limit=True)

# Define the search term and the date_since date as variables
search_words = "#stockmarket"
date_since = "2018-11-16"

# Collect tweets
tweets = tw.Cursor(api.search,
              q=search_words,
              lang="en",
              since=date_since).items(5)

# Iterate and print tweets
for tweet in tweets:
    print(tweet.text)