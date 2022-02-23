def space_it(word):

    wordx = ''
    for letter in word:
        wordx += letter + ' '
    
    return wordx.rstrip()


print(space_it('_l_p___t'))