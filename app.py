from flask import Flask, request
import * from search_for_phrases
import * from can_words_repeat

app = Flask(__name__)

@app.route( '/', methods=['POST'] )
def webhook():
    data = request.get_json()

    # We don't want to reply do ourselves!
    if( data['name'] != 'Baby DAD Bot'):
        phrase = data['text']
        check_if_salt_is_used_and_print( phrase )
        check_if_poop_is_used_and_print( phrase )
        check_if_taylor_is_used_and_print( phrase )
        check_if_meeting_is_used_and_print( phrase )
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
