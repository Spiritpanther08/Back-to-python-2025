# SQL and sqlite3 to be INSTALLED


name=input("Hi! What's your name? "+"\n") + ", welcome to the guessing game!"
import random
number_to_guess = random.randint(1, 100)
guess = input("I'm thinking of a number between 1 and 100. Can you guess what it is? "+"\n")


secret_code = "6789"
if guess == secret_code: 
    print("Developer Mode unlocked, the number guessed is " + str(number_to_guess))

while True:
    try:
        guess = int(guess)
        if guess < number_to_guess:
            guess = input("Too low! Try again: "+"\n")
        elif guess > number_to_guess:
            guess = input("Too high! Try again: "+"\n")
        else:
            print("Congratulations, " + name.split(",")[0] + "! You've guessed the number " + str(number_to_guess) + " correctly!")
            break
    except ValueError:
        guess = input("Please enter a valid number: "+"\n")

