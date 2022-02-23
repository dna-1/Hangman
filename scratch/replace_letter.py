

def replace_letters(word, letter, posns):

    # convert word to list
    word_list = list(word)

    # replace letter
    for posn in posns:
        word_list[posn] = 'p'
    
    # convert list to string
    return ''.join(word_list)




print(replace_letters('_____', 'p', (1,2)))