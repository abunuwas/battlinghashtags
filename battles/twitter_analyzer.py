try:
    import json
except ImportError:
    import simplejson as json

import time, datetime

def twitterAnalyzer(tweet):
	created_at = tweet['created_at']
	created_at_values = time.strptime(created_at,'%a %b %d %H:%M:%S +0000 %Y')
	created_at_time = datetime.datetime(year=created_at_values[0],
                                      	month=created_at_values[1],                              
                               		       day=created_at_values[2],
                         		           hour=created_at_values[3],
                                		   minute=created_at_values[4],
                                    	   second=created_at_values[5])
	created_at_time = created_at_time + datetime.timedelta(hours=1)
	#print(created_at_time, tweet['entities']['hashtags'])
	return (created_at_time, tweet['entities']['hashtags'], tweet['text'])