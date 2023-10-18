# Calculate Factorial
# Factorial: Simply represented as n!, it means multiplying all natural numbers from 1 to n.
# ex) 3! = 1*2*3, 6! = 1*2*3*4*5*6

def factorial(n):
    # Base case: Factorial of 0 and 1 is 1
    if n == 0 or n == 1:
        return 1
    else:
        # Recursive case: Factorial of n is n times factorial of (n - 1)
        return n * factorial(n - 1)

# Get input from the user
num = int(input("Enter a number: "))

# Call the factorial function to calculate the factorial of the input number
result = factorial(num)

# Print the result
print(f"The factorial of {num} is {result}")
