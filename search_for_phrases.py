import emoji
from send_message import send_message

def check_if_meeting_is_used_and_print( phrase ):
    phrase = phrase.lower()
    if( "meeting" in phrase ):
        send_message( emoji.emojize( ":rose::beer_mug::cactus:\n:rose::beer_mug::cactus:", use_aliases = True ) )

def check_if_taylor_is_used_and_print( phrase ):
    phrase = phrase.lower()
    if( "taylor" in phrase ):
        send_message( emoji.emojize( "Actually it's\n:sparkles::cocktail_glass: Tequila Holiday :cocktail_glass::sparkles:", use_aliases = True ) )

def check_if_salt_is_used_and_print( phrase ):
    phrase = phrase.lower()
    if( ( "salt" in phrase ) or ( "salty" in phrase ) ):
        send_message( "https://media.giphy.com/media/3o7P4F86TAI9Kz7XYk/giphy.gif" )
    return

def check_if_poop_is_used_and_print( phrase ):
    phrase = phrase.lower()
    if( "poop" in phrase ):
        send_message( emoji.emojize( ":pile_of_poo: spoopy :pile_of_poo:" ) )
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
        if( len( word ) > 1 ):
            if( word == 'i\'m' or word == 'im' or ( ord( word[1] ) == 8217 ) ):
                return position
    return -1
