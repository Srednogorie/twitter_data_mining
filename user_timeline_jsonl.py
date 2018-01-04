# Chap02-03/twitter_get_user_timeline.py

# Run this script with the fowolling command:
# python user_timeline_jsonl.py PacktPub
# user_timeline() -> max of 3200 tweets count=200 pages(16) 200x16=3200

import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/..')
import json
from tweepy import Cursor
from twitter.twitter_client import get_twitter_client

if __name__ == '__main__':
    user = sys.argv[1]
    client = get_twitter_client()

    fname = "user_timeline_{}.jsonl".format(user)

    with open(fname, 'w') as f:
        for page in Cursor(client.user_timeline, screen_name=user,
                           count=200).pages(16):
            for status in page:
                f.write(json.dumps(status._json) + "\n")