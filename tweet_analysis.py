import tweepy
from textblob import TextBlob


# Use below info from your own Twitter app.

consumer_API_key = 'zhEVl9ytVdxVfx7OjFEtIQTVR'
consumer_API_secret = 'Nw5bMopC2LMIiWh73InpAbUipLNWt4CVeGZaAZL3zKqla3Secx'
access_token = '731014990539464704-b5Lyomzm6UIiBKImxW80SaEgR7DEQpW'
access_token_secret = '8WyxYTNq5nDI9Vzt8HMtMwQVLJ4h3Eeatqq9GlKUCeDwm'



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
