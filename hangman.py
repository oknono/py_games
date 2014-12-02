# -*- coding: utf-8 -*-

#Code for the game "Hangman", inspired by the book "Invent with Python"
#Some adjustments made in logic, structure and naming conventions

import random #needed to select a random word from a list

play_again = True

# Following copy/pasted from book

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

words = '''ant baboon badger bat bear beaver camel cat clam cobra cougar coyote 
crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama 
mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram 
rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger 
toad trout turkey turtle weasel whale wolf wombat zebra'''.split()

def get_random_word(word_list):
    return word_list[random.randint(0,len(word_list)-1)]
    
def draw_board(HANGMANPICS, missed_letters, correct_letters, secret_word):
    print HANGMANPICS[len(missed_letters)]
    print 
    # print wrong guesses 
    print "Missed letter:",
    for letter in missed_letters:
        print letter,
    print 
    # print secret word with blanks for unguessed letters and letter for correct choices
    for i in range(len(secret_word)):
        if secret_word[i] in correct_letters:
            print secret_word[i],
        else:
            print "_",
    print

def get_guess(string):
    while True:
        guess = raw_input("Guess a letter : ").lower()
        if len(guess)!= 1:
            print "Please enter a single letter!"
        elif guess in string:
            print "You have already guessed this letter! Please guess again!"
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
        	print "Please enter a letter!"
        else:
            return guess
    
# This is the main game. The variable play again is set to True Default
# At the end of a game a player can choose to play again or stop
while play_again:
	# setup of variables and print stuff
    print
    print "WELCOME to H A N G M A N!"
    secret_word = get_random_word(words)
    missed_letters = ''
    correct_letters = ' ' 
    # print secret_word
	# This is where computer draws board, and user guesses. Use to breaks to get
	# out of the while loop. Break when win or lose
    while True:
        draw_board(HANGMANPICS, missed_letters, correct_letters, secret_word)
        guess = get_guess(missed_letters + correct_letters)
        
        # option 1: guess is in secret word - add to list and check for win
        if guess in secret_word:
            correct_letters += guess
            found_all_letters = True
            for i in range(len(secret_word)):
                if secret_word[i] not in correct_letters:
            	    found_all_letters = False
            	    break
            if found_all_letters:
            	print "You win! The secret word is %s!" %secret_word
            	break
               
        #option 2: guess is not in secret word - add to list and check for loss
        else:
            missed_letters += guess
            if len(missed_letters) == len(HANGMANPICS)-1:
                draw_board(HANGMANPICS, missed_letters, correct_letters, secret_word)
                print '''You have run out of guesses after %s correct guesses and %s 
wrong guesses. The secret word was %s''' %(len(correct_letters), len(missed_letters), secret_word)
                break
                
    print
    # present player with option to play again
    play_again = raw_input("Do you want to play again?(Y)es/(N)o: ").lower().startswith('y')
	
