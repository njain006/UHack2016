import oauth2 as oauth
import json
import codecs

# Import the necessary methods from "twitter" library
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

CONSUMER_KEY = "QykfpJa9UUvp9tP44BK3UaF5f"
CONSUMER_SECRET = "Yl9sqzRKs0fLG1q8sgczjbt4r44Xu2UFGu9Otg6oTSGM6fHrH6"

ACCESS_KEY = 	"17414102-MXCD5KJaxJwchcGbqxN1ADHEvgL8Piou007GXoM4Z"
ACCESS_SECRET = 	"Bn4gzk0YTWMkX5wdW4sga16dWHpmihJ5nkWGRoJEgA6iA"

consumer = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
access_token = oauth.Token(key=ACCESS_KEY, secret=ACCESS_SECRET)

oauth = OAuth(ACCESS_KEY, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)    

# Initiate the connection to Twitter Streaming API
twitter_stream = TwitterStream(auth=oauth)

# Get a sample of the public data following through Twitter
iterator = twitter_stream.statuses.sample()

# Print each tweet in the stream to the screen 
# Here we set it to stop after getting 1000 tweets. 
# You don't have to set it to stop, but can continue running 
# the Twitter API to collect data for days or even longer. 
tweet_count = 1000
for tweet in iterator:
    tweet_count -= 1
    # Twitter Python Tool wraps the data returned by Twitter 
    # as a TwitterDictResponse object.
    # We convert it back to the JSON format to print/score
    #print (json.dumps(tweet)  )
    
    # The command below will do pretty printing for JSON data, try it out
    # print json.dumps(tweet, indent=4)
       
    if tweet_count <= 0:
        break