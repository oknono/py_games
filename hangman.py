# -*- coding: utf-8 -*-

import random

# Code for hangman

# Words are provided in a list, and images copied from book

# list of images used, sequentially 0 - 6, corresponds to no. of wrong guesses

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
  
# secret word is randomly selected from list
# the split makes "words" a list where every word is an item (easier to manage a long string

words = '''ant baboon badger bat bear beaver 
camel cat clam cobra cougarcoyote crow deer dog
donkey duck eagle ferret fox frog goat goose hawk
lion lizard llama mole monkey moose mouse mule newt
otter owl panda parrot pigeon python rabbit ram rat
raven rhino salmon seal shark sheep skunk sloth snake
spider stork swan tiger toad trout turkey turtle weasel
whale wolf wombat zebra'''.split()

# Don't hardcode length of list. Select a word from list by randomly choose a key
#
def get_random_word(word_list):
	return word_list[random.randint(0,len(word_list)-1)]
	
# Draw "board" - image, guessed letters and missed letters
# This function is going to be called everytime the users does something and redrawn

def display_board(HANGMANPICS, missed_letters, correct_letters, secret_word):
    print HANGMANPICS[len(missed_letters)]
    print 
    print "Missed letter:",
    for letter in missed_letters:
    	print letter,
    print 
    for i in range(len(secret_word)):
    	if secret_word[i] in correct_letters:
    		print secret_word[i],
    	else:
    		print "_",
#   blanks = "_" * len(secret_word)
#	for i in range(len(secret_word)):		
#		if secret_word[i] in correct_letters:
#			blanks = blanks[:i] + secret_word[i] + blanks[i+1:]
#	for letter in blanks:
#		print letter,
#	print 
#
# Get user input - check:
# - is input ONE letter
# - has letter been guessed before
# - is letter in word or not
def get_guess(already_guessed):
	guess = raw_input("Guess a letter: ")
    if len(guess) != 1:
		print "Please enter a single letter."
	#elif guess in already_guessed:
  	#	print "You have already guessed that letter. Choose another letter"
 	#elif guess not in 'abcdefghijklmnopqrstuvwxyz':
    #   	print "Please enter a LETTER."
    else:
    	return guess
        	
def playAgain():
	 play_again = raw_input("Do you want to play again? (yes or no): ").lower()
     return play_again.startswith('y')

# start the game
# print "H A N G M A N"
# missed_letters = ''
# correct_letters = ''
# secret_word = get_random_word(words)
# game_is_done = False

# while True:
#	display_board(HANGMANPICS, missed_letters, correct_letters, secret_word)
#	guess = get_guess(missed_letters + correct_letters)
#	
#	if guess in secret_word:
#		correct_letters += guess
#		
#		found_all_letters = True
#		for i in range(len(secret_word)):
#			if secret_word[i] not in correct_letters:
#				found_all_letters = False
#				break
#		if found_all_letters:
#			print "Yes! The secret word is %s! You have won" %secret_word
#			game_is_done = True
#	else:
#		missed_letters += guess
#		
#		if len(missed_letters) == len(HANGMANPICS)-1:
#			display_board(HANGMANPICS, missed_letters, correct_letters, secret_word)
#			print "You have run out of guesses!\nAter %s missed guesses \
#		    and %s correct guesses, the word was \"%s\"" %(len(missed_letters), len(correct_letters), secret_word)
#		    game_is_done = True
#		
#	if game_is_done:
#		if play_again():
#			missed_letters = ''
#			correct_letters = ''
#			game_is_done = False
#			secret_word = get_random_word(words)
#		else:
#			break