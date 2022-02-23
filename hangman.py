import time
import random

HANGMAN_PICS = ['''
  +---+
      |
      |
      |
     ===''', '''
  +---+
  O   |
      |
      |
     ===''', '''
  +---+
  O   |
  |   |
      |
     ===''', '''
  +---+
  O   |
 /|   |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
 /    |
     ===''', '''
  +---+
  O   |
 /|\  |
 / \  |
     ===''', '''
  +---+
 [O   |
 /|\  |
 / \  |
     ===''', '''
  +---+
 [O]  |
 /|\  |
 / \  |
     ===''']


fruit = ['strawberry', 'kumquat', 'banana', 'orange', 'pineapple', 'grapefruit', 'avocado', 'blackberry', 'blueberry', 'gooseberry', 'hazelnut', 'clementine', 'raspberry']
vegetable = ['cabbage', 'asparagus', 'cauliflower', 'cucumber', 'pumpkin', 'parsnip', 'spinach', 'eggplant', 'ratatouille', 'chickweed', 'vegetable', 'asparagus']
instruments = ['saxophone', 'violin', 'clarinet', 'bagpipes', 'euphonium', 'flugelhorn', 'mandolin', 'guitar', 'synthesizer', 'trombone','xylophone', 'keyboard']
household = ['cupboard', 'wardrobe', 'shelving', 'kettle', 'radiator', 'television', 'curtains', 'staircase', 'bookshelf', 'computer', 'grinder', 'cutlery']
outside = ['motorway', 'roundabout', 'skyscrapper', 'fencing', 'statue', 'chimney', 'building', 'pavement', 'crossing', 'carpark', 'household', 'bedroom']
creatures = ['aardvark', 'anteater', 'cheater', 'dragonfly', 'alligator', 'griffon', 'penguin', 'grasshopper', 'leopard', 'kangaroo', 'gorilla', 'beaver']

dictionary = fruit + vegetable + instruments + household + outside + creatures

def get_letter():
    """
    Gets a letter from the user, will only
    return an a-z character
    """
    # do until valid letter
    while True:
        letter = input('Enter a letter: ')[0]

        letter = letter.lower()

        if letter.isalpha():
            return letter
        else:
            print("You didn't enter a letter")



def letter_positions(word, letter):
    """
    finds the letter in the word and returns
    a tuple with the positon(s)
    """
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


def replace_letters(word, letter, posns):
    """
    Replaces the letter(s) in the word at the 
    position(s) given
    """
    # convert word to list
    word_list = list(word)

    # replace letter
    for posn in posns:
        word_list[posn] = letter
    
    # convert list to string
    return ''.join(word_list)


def space_it(word):

    wordx = ''
    for letter in word:
        wordx += letter + ' '
    
    return wordx.rstrip()






game_on = True

# new game
while game_on:
    
    random.shuffle(dictionary)

    secret_word = dictionary[0]

    user_word = '_' * len(secret_word)

    all_guessed_letters = ''

    wrong_guess_letters = ''

    max_wrong_guesses = 8

    num_wrong_guesses = 0

    #print('user word: ', user_word)

    # this game
    while True:

        #print('_ ' * len(secret_word) + '\n')

        hidden_letters = '_'

        print(HANGMAN_PICS[num_wrong_guesses])

        print('Wrong guesses: ', wrong_guess_letters)

        print(space_it(user_word))

        # check if all letters guessed 
        if user_word.find('_') < 0:
            print('Well done, you won!')
            break

        # check if max wrong guesses
        if num_wrong_guesses == max_wrong_guesses:
            print(f"Too many wrong guesses, the secret word was '{secret_word}', you lost!")
            break

        while True:
            # get a letter from the user
            letter = get_letter()

            # check letter not already guessed
            if all_guessed_letters.find(letter) < 0:
                all_guessed_letters += letter
                break
            else:
                print('You already guessed that letter!')

        # find and return the letter position(s), 
        # empty tuple if not found
        posns = letter_positions(secret_word, letter)

        # put the letters into user word at correct positions
        user_word = replace_letters(user_word, letter, posns)

        #print(user_word)

        # add wrong letter to wrong_guess_letters list
        if len(posns) == 0:
            wrong_guess_letters = wrong_guess_letters + letter
            num_wrong_guesses += 1
            #print(HANGMAN_PICS[num_wrong_guesses])
            #print('Wrong guesses: ', wrong_guess_letters)


        
    

    play_again = input('Do you want to play again y or n: ')[0]

    if play_again.lower() != 'y':
        game_on = False
        print('Bye!')






