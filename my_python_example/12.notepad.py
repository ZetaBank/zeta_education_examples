# Create a Notepad

import sys

# Function to write the provided memo to the 'memo.txt' file
def write_memo(memo):
    with open('memo.txt', 'a') as f:
        f.write(memo + '\n')

# Function to read the contents of the 'memo.txt' file
def read_memo():
    with open('memo.txt') as f:
        memo = f.read()
    return memo

# Function to erase all text from the 'memo.txt' file
def erase_memo():
    with open('memo.txt', 'w') as f:
        f.truncate(0)

# Main function to handle command-line arguments and perform actions
def main():
    # Get the option from the command-line argument
    option = sys.argv[1]

    if option == '-w':
        # Check if memo text is provided as an argument
        if len(sys.argv) < 3:
            print("Please provide memo text to write.")
            return
        memo = sys.argv[2]
        # Call the function to write memo to the file
        write_memo(memo)

    elif option == '-r':
        # Call the function to read memo from the file and print it
        memo = read_memo()
        print("Memo contents:\n", memo)

    elif option == '-e':
        # Call the function to erase all text from the file
        erase_memo()
        print("All text has been erased from the memo.")
        
    else:
        # Print an error message for incorrect argument
        print("Invalid argument. Use '-w' to write, '-r' to read, or '-e' to erase.")

# Ensure the main function is executed when the script is run
if __name__ == "__main__":
    main()
