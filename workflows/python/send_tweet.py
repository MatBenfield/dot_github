# importing the module
import tweepy 

# personal details 
consumer_key = ${{ secrets.tw_consumer_key }}
consumer_secret = ${{ secrets.tw_consumer_secret }}
access_token = ${{ secrets.tw_access_token }}
access_token_secret = ${{ secrets.tw_access_secret }}

# authentication of consumer key and secret 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
  
# authentication of access token and secret 
auth.set_access_token(access_token, access_token_secret) 

api = tweepy.API(auth) 

# update the status 
api.update_status(status ="Hello Everyone !") 
