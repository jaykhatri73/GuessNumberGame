import random

def guess_number():
    # generate random no.
    number = random.randint(1, 50)
    attempts = 0
    
    #greeting and setting boundries from 1 to 50
    print("Lets Play the game of Guessing the Number.")
    print("I'm thinking of a number between 1 and 50. Can you guess it?")
    print("You have only 5 attempts to guess the number")
    
    
    # condition on attempts
    while attempts < 5:
        guess = input("Take a guess: ")
        try:
            guess = int(guess)
    
        # catch value error 
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        attempts += 1

        if guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            return

    print(f"Sorry, you ran out of attempts! The number I was thinking of was {number}.")

guess_number()
