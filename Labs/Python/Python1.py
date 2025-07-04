# Level 1: Getting familiar with Python syntax

# Exercise 1: Print "Hello, World!"
# This program prints the classic "Hello, World!" message to the console.
print("Hello, World!")

print("\n" + "="*30 + "\n") # Separator for clarity

# Exercise 2: Calculate the sum of 2 numbers
# This program takes two numbers as input from the user,
# converts them to integers, and then prints their sum.
try:
    num1_str = input("Enter the first number: ")
    num2_str = input("Enter the second number: ")

    # Convert input strings to integers
    num1 = int(num1_str)
    num2 = int(num2_str)

    # Calculate the sum
    sum_of_numbers = num1 + num2

    # Print the result
    print(f"The sum of {num1} and {num2} is: {sum_of_numbers}")
except ValueError:
    print("Invalid input. Please enter valid integer numbers.")

print("\n" + "="*30 + "\n") # Separator for clarity

# Exercise 3: Calculate the area of a circle
# This program takes the radius of a circle as input,
# calculates its area using the formula A = π * r^2, and prints the result.
import math # Import the math module to access math.pi

try:
    radius_str = input("Enter the radius of the circle: ")

    # Convert input string to a float
    radius = float(radius_str)

    # Ensure radius is non-negative
    if radius < 0:
        print("Radius cannot be negative. Please enter a positive number.")
    else:
        # Calculate the area
        area = math.pi * (radius ** 2) # ** is the exponentiation operator

        # Print the result, formatted to two decimal places
        print(f"The area of a circle with radius {radius} is: {area:.2f}")
except ValueError:
    print("Invalid input. Please enter a valid number for the radius.")

print("\n" + "="*30 + "\n") # Separator for clarity

# Exercise 4: Check if a number is even/odd
# This program takes an integer as input and determines if it's even or odd.
# An even number is perfectly divisible by 2 (remainder is 0).
# An odd number has a remainder of 1 when divided by 2.
try:
    number_str = input("Enter an integer to check if it's even or odd: ")

    # Convert input string to an integer
    number = int(number_str)

    # Check if the number is even or odd using the modulo operator (%)
    if number % 2 == 0:
        print(f"The number {number} is Even.")
    else:
        print(f"The number {number} is Odd.")
except ValueError:
    print("Invalid input. Please enter a valid integer.")

print("\n" + "="*30 + "\n") # Separator for clarity

# Exercise 5: Swap the values of two variables without using a temporary variable
# This program demonstrates two common ways to swap variables in Python:
# 1. Using arithmetic operations (for numbers)
# 2. Using tuple unpacking (the most Pythonic way, works for any data type)

# Method 1: Using arithmetic operations (only works for numbers)
print("--- Swapping using arithmetic operations ---")
a = 5
b = 10
print(f"Before swap (arithmetic): a = {a}, b = {b}")
a = a + b  # a becomes 15 (5 + 10)
b = a - b  # b becomes 5 (15 - 10)
a = a - b  # a becomes 10 (15 - 5)
print(f"After swap (arithmetic): a = {a}, b = {b}")

print("\n--- Swapping using tuple unpacking (Pythonic way) ---")
x = "Hello"
y = "World"
print(f"Before swap (unpacking): x = '{x}', y = '{y}'")
x, y = y, x # This is equivalent to: temp = x; x = y; y = temp
print(f"After swap (unpacking): x = '{x}', y = '{y}'")