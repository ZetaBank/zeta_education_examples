# Rock, Paper, Scissors battle

import random

# Function to determine the winner of the game
def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == "r" and computer_choice == "s") or \
         (player_choice == "p" and computer_choice == "r") or \
         (player_choice == "s" and computer_choice == "p"):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    # Print the welcome message and game instructions
    print("Welcome to Rock-Paper-Scissors!")
    print("Enter 'r' for rock, 'p' for paper, 's' for scissors, or 'q' to quit.")
    
    choices = ["r", "p", "s"]  # Possible choices for the game
    
    while True:
        player_choice = input("Your choice: ").lower()
        
        # Check if the player wants to quit
        if player_choice == "q":
            print("Thanks for playing!")
            break
        
        # Check if the player's choice is valid
        if player_choice in choices:
            computer_choice = random.choice(choices)  # Randomly select computer's choice
            
            print(f"You chose: {player_choice}")
            print(f"Computer chose: {computer_choice}")
            
            result = determine_winner(player_choice, computer_choice)  # Determine the winner
            print(result)  # Display the result of the game
        else:
            print("Invalid choice. Please enter 'r', 'p', 's', or 'q' to quit.")

if __name__ == "__main__":
    main()  # Run the main game loop
