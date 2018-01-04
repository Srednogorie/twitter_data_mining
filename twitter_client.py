# Chap02-03/twitter_client.py
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/..')
from tweepy import API
from tweepy import OAuthHandler
import twitter.credentials as credentials


def get_twitter_auth():
    """Setup Twitter authentication.

    Return: tweepy.OAuthHandler object
    """
    auth = OAuthHandler(credentials.consumer_key, credentials.consumer_secret)
    auth.set_access_token(credentials.access_token, credentials.access_token_secret)
    return auth


def get_twitter_client():
    """Setup Twitter API client.

    Return: tweepy.API object
    """
    auth = get_twitter_auth()
    client = API(auth)
    return client