import random
x=random.randint(1, 10)
loop=True

while(loop==True):
	guess=input("Guess integer between 1 and 10: ")
	if int(guess) == x:
		print("Correct! it was "+str(x))
		loop=False
	elif int(guess) > x:
		print("Incorrect, Your guess is too high. Try again...")
	else:
		print("Incorrect, Your guess is too low. Try again.")

		#we're changing something
	print("A Change!")
	
	