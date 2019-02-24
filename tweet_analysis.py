import tweepy
from textblob import TextBlob


# Use below info from your own Twitter app.

consumer_API_key = 'zhEVl****************'
consumer_API_secret = 'Nw5bMo**************************ecx'
access_token = '73101*****************************EgR7DEQpW'
access_token_secret = '*********************************UCeDwm'



# Authenticate your application

auth = tweepy.OAuthHandler(consumer_API_key, consumer_API_secret)
# Set access token for consumer key
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Searching for specific tweets to which we need to analyse
# Let's analyse Elon's tweets because, why not.
public_tweets = api.search('Elon Musk')
for tweet in public_tweets:
    # print tweets
    print(tweet.text)
    # Use textblob to fetch sentimental of the tweet
    analyse = TextBlob(tweet.text)
    print(analyse.sentiment)
    print('\n')
