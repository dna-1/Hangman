def get_positions(word, letter):

    posns = ()
    start = 0

    # keep looping until all letters found
    while True:

        posn = word.find(letter, start)

        # if letter not found (-1)
        if posn < 0:
            return posns
        else:
            posns = posns + (posn,) # add to tuple
            start = posn + 1


posns = get_positions('apple', 'p')

print(posns)