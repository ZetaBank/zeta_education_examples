# Guess the Digits
# ex) 4 -> 1 digit, 100 -> 3 digits, 7777 -> 4 digits

def count_digits(number):
    if number == 0:
        return 1  # Special case for the number 0 (which has 1 digit)
    
    count = 0  # Initialize a count to track the number of digits
    
    # Loop to count digits by repeatedly dividing the number by 10
    while number > 0:
        count += 1         # Increment the digit count
        number //= 10      # Remove the least significant digit by integer division
    
    return count  # Return the total count of digits

# Get input from the user
input_str = input("Enter a positive integer: ")

# Check if the input is a positive integer
if input_str.isdigit():
    input_number = int(input_str)
    
    # Check for non-positive input
    if input_number <= 0:
        print("Please enter a positive integer.")
    else:
        # Calculate the number of digits using the count_digits function
        num_digits = count_digits(input_number)
        print(f"The number {input_number} has {num_digits} digits.")
else:
    print("Invalid input. Please enter a positive integer.")
