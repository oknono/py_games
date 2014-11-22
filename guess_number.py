import random

computer_guess = random.randint(1,20)
guess_total = 0

name = raw_input("What is your name? ")

print("Hello %s ! Please guess the number between 1 and 20. You get 6 tries" %name)

while guess_total < 6 :
	guess = int(raw_input("take a guess: " ))
	guess_total += 1
	 
	if guess < computer_guess:
		print("Too low!")
	elif guess > computer_guess:
		print("Too high!")
	elif guess == computer_guess:
		break
	else:
		print("oops, something went wrong")
		
if guess == computer_guess:
	print("YESSSSS %s, you won, and it only took you %s guesses" %(name,guess_total))
else:
	print("You lose, the number I was thinking of was %s" s%computer_guess)
