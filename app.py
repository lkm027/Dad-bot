import os
import json

from urllib.parse import urlencode
from urllib.request import Request, urlopen

from flask import Flask, request

app = Flask(__name__)

@app.route( '/', methods=['POST'] )
def webhook():
    data = request.get_json()

    # We don't want to reply do ourselves!
    if( data['name'] != 'Baby DAD Bot'):
        phrase = data['text']
        check_if_poop_is_used_and_print( phrase )
        location = check_if_im_is_used_and_get_position( phrase )
        if( location == -1 ):
            location = check_if_i_am_is_used_and_get_position( phrase )
        if( location is not -1 ):
            words = str.split( phrase )
            if( location + 1 < len( words ) ):
                if( location + 2 < len( words ) ):
                    check_if_words_can_be_repeated( words[ location + 1 ], words[ location + 2 ] )
                else:
                    check_if_words_can_be_repeated( words[ location + 1 ], '' )

    return "ok", 200

def send_message( msg ):
    url = 'https://api.groupme.com/v3/bots/post'

    data = {
            'bot_id' : os.getenv( 'GROUPME_BOT_ID'),
            'text'   : msg,
            }
    request = Request( url, urlencode( data ).encode() )
    json = urlopen( request ).read().decode()

def check_if_poop_is_used_and_print( phrase ):
    words = str.split( phrase )
    for word in words:
        word.lower()
        if( word == 'poop' ):
            send_message( '*spoopy' )
            return

def check_if_i_am_is_used_and_get_position( phrase ):
    words = str.split( phrase )
    for position, word in enumerate( words ):
        word = word.lower()
        if( word == 'am' ):
            leading_word = words[ position - 1 ]
            leading_word = leading_word.lower()
            if( leading_word == 'i' ):
                return position
    return -1

def check_if_im_is_used_and_get_position( phrase ):
    words = str.split( phrase )
    for position, word in enumerate( words ):
        word = word.lower()
        if( word == 'i\'m' or word == 'im' or ( ord( word[1] ) == 8217 ) ):
            return position
    return -1

def check_if_words_can_be_repeated( first_word, second_word ):

    # Print words ending with e
    if( check_if_word_ends_with_e( first_word ) ):
        print_dad_bot_hi_statement( first_word, '' );

    # Print phrases where first word ends in ly and second in e
    if( check_if_word_ends_with_ly( first_word ) and check_if_word_ends_with_e( second_word ) ):
        print_dad_bot_hi_statement( first_word, second_word );

    # Print words ending with ed and not ing
    if( check_if_word_ends_with_ed( first_word ) and not check_if_word_ends_with_ing( first_word ) ):
        print_dad_bot_hi_statement( first_word, '' );

    # Print words ending with y but not ly
    if( check_if_word_ends_with_y( first_word ) and not check_if_word_ends_with_ly( first_word ) ):
        print_dad_bot_hi_statement( first_word, '' )

    # Print phrase where first word ends in ly and second in y
    if( check_if_word_ends_with_ly( first_word ) and check_if_word_ends_with_y( second_word ) ):
        print_dad_bot_hi_statement( first_word, second_word )

    # Print phrase where first word ends in ly and second in ed
    if( check_if_word_ends_with_ly( first_word ) and check_if_word_ends_with_ed( second_word ) ):
        print_dad_bot_hi_statement( first_word, second_word )

def print_dad_bot_hi_statement( first_word, second_word ):
    if( not second_word ):
        send_message( 'Hi {}, I\'m Baby Dad bot!'.format( first_word ) )
    else:
        send_message( 'Hi {} {}, I\'m Baby Dad bot!'.format( first_word, second_word ) )


def check_if_word_ends_with_ed( word ):
    last_two_letters = len(word) - 2
    if( word and word[last_two_letters:].lower() == 'ed' ):
        return True
    return False

def check_if_word_ends_with_ing( word ):
    last_three_letters = len(word) - 3
    if( word and word[last_three_letters:].lower() == 'ing' ):
        return True
    return False

def check_if_word_ends_with_y( word ):
    last_letter = len( word ) - 1
    if( word and word[last_letter:].lower() == 'y' ):
        return True
    return False

def check_if_word_ends_with_ly( word ):
    last_two_letters = len(word) - 2
    if( word and word[last_two_letters:].lower() == 'ly' ):
        return True
    return False

def check_if_word_ends_with_e( word ):
    last_letter = len(word) - 1
    if( word and word[last_letter:].lower() == 'e' ):
        return True
    return False
