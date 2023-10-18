# Guess the Random Number

import random

def guess_the_number():
    # Generate a random target number between 1 and 100
    target_number = random.randint(1, 100)
    attempts = 0

    while True:
        # Get the user's guess
        user_guess = int(input("Guess the number between 1 and 100: "))
        attempts += 1

        # Compare user's guess with the target number
        if user_guess < target_number:
            print("Too low! Try again.")
        elif user_guess > target_number:
            print("Too high! Try again.")
        else:
            # User guessed the correct number
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break

# Run the function to start the guessing game
guess_the_number()
