import random
xx=random.randint(1, 10)
loopy=True

while(loopy==True):
	guess=input("Guess integer between 1 and 10: ")
	if int(guess) == xx:
		print("Correct! it was "+str(xx))
		loopy=False
	elif int(guess) > xx:
		print("Incorrect, Your guess is too high. Try again...")
	else:
		print("Incorrect, Your guess is too low. Try again.")

		#we're changing something
	print("A Change!")

	#second change

	print("Another change!")
	
	