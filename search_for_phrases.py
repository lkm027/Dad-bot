import emoji
import send_message

def check_for_keywords( phrase ):
    phrase = phrase.lower()
    if "meeting" in phrase:
        print_meeting_capture()
    if "taylor" in phrase:
        print_taylor_capture()
    if "salt" in phrase or "salty" in phrase:
        print_salt_capture()
    if "poop" in phrase:
        print_poop_capture()

def print_meeting_capture():
    send_message( emoji.emojize( ":rose::beer_mug::cactus:\n:rose::beer_mug::cactus:", use_aliases = True ) )

def print_taylor_capture():
    send_message( emoji.emojize( "Actually it's\n:sparkles::cocktail_glass: Tequila Holiday :cocktail_glass::sparkles:", use_aliases = True ) )

def print_salt_capture():
    send_message( "https://media.giphy.com/media/3o7P4F86TAI9Kz7XYk/giphy.gif" )

def print_poop_capture():
    send_message( emoji.emojize( ":pile_of_poo: spoopy :pile_of_poo:" ) )

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
