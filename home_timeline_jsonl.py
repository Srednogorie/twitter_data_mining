# Chap02-03/twitter_get_home_timeline.py

# home_timeline() -> Max of 800 tweets

import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/..')
import json
from tweepy import Cursor
from twitter.twitter_client import get_twitter_client

if __name__ == '__main__':
    client = get_twitter_client()

    with open('home_timeline.jsonl', 'w') as f:
        for page in Cursor(client.home_timeline, count=200).pages(4):
            for status in page:
                f.write(json.dumps(status._json) + "\n")