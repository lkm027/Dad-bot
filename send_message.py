import os

from urllib.parse import urlencode
from urllib.request import Request, urlopen

def send_message( msg ):
    url = 'https://api.groupme.com/v3/bots/post'

    data = {
            'bot_id' : os.getenv( 'GROUPME_BOT_ID'),
            'text'   : msg,
            }
    request = Request( url, urlencode( data ).encode() )
    json = urlopen( request ).read().decode()

def print_dad_bot_hi_statement( first_word, second_word ):
    if( not second_word ):
        send_message( 'Hi {}, I\'m Baby Dad bot!'.format( first_word ) )
    else:
        send_message( 'Hi {} {}, I\'m Baby Dad bot!'.format( first_word, second_word ) )

