#importing the necessary modules
import tweepy

#authenticating
consumer_key=''
consumer_secret=''
access_token=''
access_token_secret=''
auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api=tweepy.API(auth)

#posting on twitter with image and status
api.update_with_media('image path', status="your tweet")
