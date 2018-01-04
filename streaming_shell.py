import tweepy
import json

# Authentication details. To  obtain these visit dev.twitter.com
consumer_key = 'sk5h3aKTyje7Ffk8CwZa6vMtT'
consumer_secret = '5tHSJqEKxYc08bbWYfalFcBgoJ1E7y4lL3aLlH698Nx3wce5e6'
access_token = '287175928-IL2DnvCppJBM68iJHUgMl5svVzBj5RKM0qZrZUcv'
access_token_secret = 'TADqHOjlxhrQupHxaCxiyfxO6nAk29hXz03Xa00Jr8SXj'

# This is the listener, resposible for receiving data
class StdOutListener(tweepy.StreamListener):
    def on_data(self, data):
        # Twitter returns data in JSON format - we need to decode it first
        decoded = json.loads(data)

        # Also, we convert UTF-8 to ASCII ignoring all bad characters sent by users
        #print('@%s: %s' % (decoded['user']['screen_name'], decoded['text'].encode('ascii', 'ignore')))
        #print('@%s: %s' % (decoded['user']['screen_name'], decoded['text'].encode('utf-8', 'ignore')))
        print('@%s: %s' % (decoded['user']['screen_name'], decoded['text']))
        print('')
        return True

    def on_error(self, status):
        print (status)

if __name__ == '__main__':
    l = StdOutListener()
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    print ("Showing all new tweets for #programming:")

    # There are different kinds of streams: public stream, user stream, multi-user streams
    # In this example follow #programming tag
    # For more details refer to https://dev.twitter.com/docs/streaming-apis
    stream = tweepy.Stream(auth, l)
    #stream.filter(track=['programming'])
    stream.filter(languages=["bg"], track=["за", "най", "по", "как", "искам"])  # Up tp 400 words