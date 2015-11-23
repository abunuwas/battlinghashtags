import json

from twitter_streaming import *
from twitter_analyzer import twitterAnalyzer


##twitter_stream = Stream(auth, MyListener())
##twitter_stream.filter(track=['#android', '#cat'])

e=0
with open('data.json', 'r') as f:
    line = f.readline()
    tweet = json.loads(line)
    created_at, hashtags = twitterAnalyzer(tweet)
    print(created_at)
    for hashtag in hashtags:
        if hashtag['text'] == 'cat':
            print(hashtag['text'])
