import praw
import pprint
import random
import os

from send_message import send_message

def get_joke_and_send():
    reddit = praw.Reddit( client_id = os.getenv( 'REDDIT_CLIENT_ID' )
                            client_secret = os.getenv( 'REDDIT_CLIENT_SECRET' ),
                            user_agent = os.getenv( 'REDDIT_USER_AGENT' ) )

    jokes = []
    for submission in reddit.subreddit( 'jokes' ).hot( limit=10 ):
        if not submission.distinguished:
            jokes.append( submission )

    joke = random.choice( jokes )

    send_joke( joke )

def send_joke( joke ):
    send_message( "{}/n{}".format( joke.title, joke.selftext )

# if joke.distinguished:
#     print "ew"
# print joke.title
# print joke.selftext
