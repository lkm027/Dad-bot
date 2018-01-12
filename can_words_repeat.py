from send_message import print_dad_bot_hi_statement

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
