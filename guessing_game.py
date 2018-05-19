import random

random_num = random.randint(1,10)

while True:
	guess = input("Select a number between 1 to 10: ")
	guess = int(guess)
	if guess < random_num:
		print("Too low")
	elif guess > random_num:
		print("Too high")
	else:
		print("You win")

		try_again = input("Do you want to have a one more guess: (y/n) ")
		if try_again=="y":
			random_num = random.randint(1,10)
			guess = None
		else:
			print("Thank you!! Try again")
			break