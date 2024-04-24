import random

number =  random.randrange(1,10)

guessnumbers = int(input("Guess a number:"))

while guessnumbers != number:

	if guessnumbers != number:
		print("guess again")
		
	
	else:
		print("congratulation")

	guessnumbers = int(input("Guess a number:"))
