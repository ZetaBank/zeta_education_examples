# Print Diamond Figure

def print_diamond(n):
    for i in range(n):
        spaces = abs(n // 2 - i)  # Calculate the number of spaces needed on each side
        
        # Calculate the number of diamonds needed in the middle based on spaces
        diamonds = n - 2 * spaces
        
        # Print the row with appropriate spaces and diamonds pattern
        print("□" * spaces + "■" * diamonds + "□" * spaces)

# Get user input for the size of the diamond
n = int(input("Enter Number (odd number) : "))

# Check if the input is a positive odd integer
if n % 2 == 0 or n <= 0:
    print("Please enter a positive odd integer.")
else:
    print_diamond(n)  # Print the diamond pattern
