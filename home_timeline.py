import sys
import os
import json
from pprint import pprint
#sys.path.append("/private/var/root/Python/social_mining")  This two are the same!
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/..')
from tweepy import Cursor
from twitter.twitter_client import get_twitter_client


if __name__ == '__main__':
    client = get_twitter_client()

    for status in Cursor(client.home_timeline).items(10):
        # Process a single status
        pprint(status._json)
        #pprint(status._json['entities']['hashtags'])
        #pprint(status._json['id'])
