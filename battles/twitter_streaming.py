try:
    import json
except ImportError:
    import simplejson as json

import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener

import time
import datetime

from .models import Battle, Hashtag, Tweet
from .twitter_analyzer import twitterAnalyzer


ACCESS_TOKEN = ''
ACCESS_SECRET = ''
CONSUMER_KEY = ''
CONSUMER_SECRET = ''

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tweepy.API(auth)

from django.utils import timezone

class MyListener(StreamListener):
    def __init__(self, hashtag1, hashtag2, battle, time_span=0, 
                  current_time=datetime.datetime.now(), final_time=0):
        self.time_span = datetime.timedelta(seconds=time_span)
        self.current_time = current_time
        self.final_time = self.current_time + self.time_span
        self.hashtag1 = hashtag1
        self.hashtag1_id = hashtag1.id
        self.hashtag1_text = hashtag1.hashtagText
        self.hashtag2 = hashtag2
        self.hashtag2_id = hashtag2.id
        self.hashtag2_text = hashtag2.hashtagText
        self.battle = battle
        print(self.current_time, self.final_time)


    def on_data(self, data):
      print('on_data')
      print(datetime.datetime.now(), '-----', self.final_time)

      if datetime.datetime.now() < self.final_time:
        print('new data')
        tweet = json.loads(data)
        created_at, hashtags, text = twitterAnalyzer(tweet)

        for hashtag in hashtags:
          if self.hashtag1_text[1:].lower() == hashtag['text'].lower():
            t = Tweet(text=text, created_at=created_at, typos=0,
              battle=self.battle, hashtag=self.hashtag1)
            t.save()
            try:
              print(t.text)
            except UnicodeEncodeError:
              pass
          if self.hashtag2_text[1:].lower() == hashtag['text'].lower():
            t = Tweet(text=text, created_at=created_at, typos=0,
              battle=self.battle, hashtag=self.hashtag2)
            t.save()
            try:
              print(t.text)
            except UnicodeEncodeError:
              pass
          else:
            continue

      else:
        print('Competition ended')
        return False # This closes the stream listener

    def on_error(self, status_code):
      print('Got an error with status code: ' + str(status_code))
      return True

    def on_timeout(self):
      print('Timeout...')
      return True



