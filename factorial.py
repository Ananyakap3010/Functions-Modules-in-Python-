# Task 1: Factorial Function

# Defining a function to calculate factorial
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Taking user input
num = int(input("Enter a number: "))

# Displaying result
print(f"The factorial of {num} is: {factorial(num)}")
