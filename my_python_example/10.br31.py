# Baskin Robbins 31 Game

import random

def player_turn(total):
    while True:
        try:
            # Get the player's choice of how many numbers to pick (1, 2, or 3)
            pick = int(input("Enter 1, 2, or 3: "))
            # Check if the input is within the valid range
            if pick < 1 or pick > 3:
                print("Invalid input. Please choose 1, 2, or 3.")
                continue
            # Check if the move exceeds the game limit (31)
            if total + pick > 31:
                print("Invalid move. Try again.")
                continue
            return pick
        except ValueError:
            print("Invalid input. Please enter a number.")

def computer_turn(total):
    # Calculate the maximum number of picks the computer can make
    max_pick = min(3, 31 - total)
    # Generate a random number of picks for the computer's turn
    return random.randint(1, max_pick)

def main():
    total = 0
    player_turns = True

    print("Welcome to Baskin Robbins 31!")

    while total < 31:
        if player_turns:
            print(f"Current total: {total}")
            # Get the player's turn choice
            pick = player_turn(total)
        else:
            # Get the computer's turn choice
            pick = computer_turn(total)
            print(f"Computer picks: {pick}")

        # Update the total count
        total += pick
        # Switch turns between player and computer
        player_turns = not player_turns

    # Determine the winner based on the last turn
    if player_turns:
        print("You win!")
    else:
        print("Computer wins!")

if __name__ == "__main__":
    main()
