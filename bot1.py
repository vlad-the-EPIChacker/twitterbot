# Import the necessary package to process data in JSON format
try:
    import json
except ImportError:
    import simplejson as json

import sys
import operator

# Import the necessary methods from "twitter" library
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

def getToken(fileName):
    f=open(fileName)
    file=f.readlines()
    oauth=''
    for i in file:
        i=i.strip()
        oauth=oauth+i
    token=json.loads(oauth)

# create oauth token
    oauth = OAuth(token['ACCESS_TOKEN'], token['ACCESS_SECRET'], token['CONSUMER_KEY'], token['CONSUMER_SECRET'])
    return oauth

oauth=getToken('access_token.json')
twitter = Twitter(auth=oauth)
username=sys.argv[1]
cases=100
iterator = twitter.statuses.user_timeline(screen_name = username, count=cases)
count=0
tweets=[]
for tweet in iterator:
    tweets.append(tweet)
    count=count+1
    if count>cases:
        break

top=10
count1=0
tweets=sorted(tweets,key=operator.itemgetter('retweet_count'), reverse=True)
print 'total tweets:', len(tweets)
for i in tweets:
    print i['created_at'], i['text'], i['retweet_count']
    count1=count1+1
    if count1>top:
        break