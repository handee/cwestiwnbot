import tweepy
from secrets import *
from cwestiwn import *

c=cwestiwn()

botname="@cwestiwnbot"

# Welsh question answering bot, derived heavily from this 
# "how to write a bot in python" tutorial
# https://scotch.io/tutorials/build-a-tweet-bot-with-python
# which is responsible for all the twitter interaction
# (but none of the Welsh)


# create an OAuthHandler instance
# Twitter requires all requests to use OAuth for authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 

auth.set_access_token(access_token, access_secret)

#Construct the API instance
api = tweepy.API(auth) # create an API object


def panic_tweet(string_to_tweet):
    api.update_status(string_to_tweet) 

# create a class inheriting from the tweepy  StreamListener
class BotStreamer(tweepy.StreamListener):
    # Called when a new status arrives which is passed down from the on_data method of the StreamListener
    def on_status(self, status):
        username = status.user.screen_name
        status_id = status.id

        # entities provide structured data from Tweets including resolved URLs, media, hashtags and mentions without having to parse the text to extract that information
        print(status.text)
        atstring=botname+" "
        usertext=status.text.replace(atstring,"") 
        try: 
            tweetout=c.tweeted_at(status.user.screen_name,usertext)
            panic_tweet(tweetout)
        except tweepy.TweepError as error:
            if error.api_code == 187:
        # Do something special
                print('duplicate message')
            else:
                raise error

    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_error disconnects the stream
            panic_tweet("wups, mae bot yn wedi crashio achos error 420") 
            return False
        if status_code == 187:
            print("duplicate")
            panic_tweet("Da Iawn, all good, nothing to see here")
            return True


myStreamListener = BotStreamer()

 #Construct the Stream instance
stream = tweepy.Stream(auth, myStreamListener)

stream.filter(track=[botname] )

