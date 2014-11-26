# -*- coding: utf-8 -*-

import random

# Code for hangman

# Words are provided in a list, and images copied from book

# list of images used, used sequentially 0 - 6

HANGMANPICS = ['''

   +---+
   |   |
       |
       |
       |
       |
=========''', '''
 
   +---+
   |   |
   O   |
       |
       |
       |
=========''', '''

   +---+
   |   |
   O   |
   |   |
 	   |
       |
 =========''', '''

   +---+
   |   |
   O   |
  /|   |
 	   |
       |
 =========''', '''
￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼
   +---+
   |   |
   O   |
  /|\  |
 	   |
       |
 =========''', '''
 
   +---+
    |   |
    O   |
   /|\  |
   /    |
        |
  =========''', '''
 
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
  =========''']
  
# Generate secret word - the split makes it a list where every word is an item

words = '''ant baboon badger bat bear beaver 
camel cat clam cobra cougarcoyote crow deer dog
donkey duck eagle ferret fox frog goat goose hawk
lion lizard llama mole monkey moose mouse mule newt
otter owl panda parrot pigeon python rabbit ram rat
raven rhino salmon seal shark sheep skunk sloth snake
spider stork swan tiger toad trout turkey turtle weasel
whale wolf wombat zebra'''.split()

# Don't hardcode length of list. Select a word from list by randomly choose a key
def get_random_word(word_list):
	return word_list[random.randint(0,len(word_list)-1)]
	
# Draw "board" - image, guessed letters and missed letters
# This function is going to be called everytime the users does something and redrawn

def display_board(HANGMANPICS, missed_letters, correct_letters, secret_word):
    print HANGMANPICS[len(missed_letters)]
    print ()
    print "Missed letter:", end=" "
    	for letter in missed_letters:
    		print letter, end = ''
	print ()
# board image 0 t/m 6
# blanks "_ " * len(secret_word)

# Get user input
# letter is in word

# letter is not in word
# letter has been guessed before
# input is not a letter

# Player guessed all letters right before time runs out. WIN

# Player hasn't guessed the word and LOSES

# Play again? -> Same loop as dragon game

secret_word = words[random.randint(0,len(words))]
print secret_word