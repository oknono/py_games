import random
import time

def displayIntro():
	print(''' \nYou are in a land filled with MONSTERS. In front
of you you see two caves. One cave houses a FRIENDLY monster,
that will share cake and balloons with you. The OTHER cave 
though... houses an EVIL monster that will eat you on sight.\n''')

	
def chooseCave():
	cave = raw_input("Do you choose cave 1 or 2? ")
	
	if cave != "1" and cave != "2":
		chooseCave()
	else:
		return checkCave(int(cave))

def checkCave(chosenCave):
	print('You approach the cave...')
	time.sleep(3)
	print('It is dark and spooky...')
	time.sleep(3)
	print('A large monster out in front of you! He opens his jaws and... \n')
	time.sleep(2)
	
	friendlyCave = random.randint(1,2)
	
	if chosenCave == friendlyCave:
		print("Showers you with champagne! Good choice young one!\n")
	else:
		print("EATS YOU UP AND SPITS YOU OUT!\n")

play_again = True

while play_again == True:

	displayIntro()
	chooseCave()
	play = raw_input("Do you want to play again? (y)es or (n)o: ")
	if play == 'yes' or play == 'y':
		play_again = True
	else:
		play_again = False


