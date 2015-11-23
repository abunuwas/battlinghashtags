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


ACCESS_TOKEN = '453873532-wAUWfgUdWjNc1fYuDk9WY3GoSd4HV0iCpzdGtifJ'
ACCESS_SECRET = 'JknLL0m9uSDgPeGj9JOtxUuDjiVrUjHxe6wOHQniAlKy2'
CONSUMER_KEY = 'uGzNknNhK6LQh2EIzZX4vuUBI'
CONSUMER_SECRET = 'MZgRHdYQzAwh8IO0pFDchsfX4ECxhazXB1vJqZMQuYF46UkOA7'

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tweepy.API(auth)

from django.utils import timezone

class MyListener(StreamListener):
    def __init__(self, time_span=0, current_time=datetime.datetime.now(), 
                  final_time=0, hashtag1, hashtag2, battle_id):
        self.time_span = datetime.timedelta(seconds=time_span)
        self.current_time = current_time
        self.final_time = self.current_time + self.time_span
        self.hashtag1 = hashtag1
        self.hashtag2 = hashtag2
        self.battle_id = battle_id
        print(self.current_time, self.final_time)


    def on_data(self, data):
        if datetime.datetime.now() < self.final_time:
          tweet = json.loads(data)
          created_at, hashtags, text = twitterAnalyzer(tweet)
          
          


        else:
          print('Competition ended')
          return False # This closes the stream listener

    def on_error(self, status_code):
      print('Got an error with status code: ' + str(status_code))
      return True

    def on_timeout(self):
      print('Timeout...')
      return True



