print("\n" + "="*30 + "\n") # Separator for clarity
print("--- Level 2: Flow Control, Loops, Functions ---")

# Exercise 6: Find the largest of 3 numbers
# This program takes three numbers as input and prints the largest among them.
try:
    num1_l2_str = input("Enter the first number (for largest): ")
    num2_l2_str = input("Enter the second number (for largest): ")
    num3_l2_str = input("Enter the third number (for largest): ")

    num1_l2 = int(num1_l2_str)
    num2_l2 = int(num2_l2_str)
    num3_l2 = int(num3_l2_str)

    # Using if-elif-else to find the largest
    if num1_l2 >= num2_l2 and num1_l2 >= num3_l2:
        largest = num1_l2
    elif num2_l2 >= num1_l2 and num2_l2 >= num3_l2:
        largest = num2_l2
    else:
        largest = num3_l2

    print(f"The largest number among {num1_l2}, {num2_l2}, and {num3_l2} is: {largest}")

    # Alternative using the built-in max() function (more concise)
    # largest_alt = max(num1_l2, num2_l2, num3_l2)
    # print(f"Using max() function, the largest is: {largest_alt}")

except ValueError:
    print("Invalid input. Please enter valid integer numbers for finding the largest.")

print("\n" + "="*30 + "\n") # Separator for clarity

# Exercise 7: Print multiplication table of a number
# This program takes a number as input and prints its multiplication table from 1 to 10.
try:
    table_num_str = input("Enter a number to print its multiplication table: ")
    table_num = int(table_num_str)

    print(f"Multiplication Table for {table_num}:")
    for i in range(1, 11): # Loop from 1 to 10 (11 is exclusive)
        print(f"{table_num} x {i} = {table_num * i}")
except ValueError:
    print("Invalid input. Please enter a valid integer for the multiplication table.")

print("\n" + "="*30 + "\n") # Separator for clarity

# Exercise 8: Calculate factorial of a number
# This program calculates the factorial of a non-negative integer using both
# an iterative approach (for loop) and a recursive function.

# Iterative approach
def factorial_iterative(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0:
        return 1
    else:
        fact = 1
        for i in range(1, n + 1):
            fact *= i # fact = fact * i
        return fact

# Recursive approach
def factorial_recursive(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0:
        return 1
    else:
        return n * factorial_recursive(n - 1)

try:
    fact_num_str = input("Enter a non-negative integer to calculate its factorial: ")
    fact_num = int(fact_num_str)

    print(f"Factorial of {fact_num} (Iterative): {factorial_iterative(fact_num)}")
    print(f"Factorial of {fact_num} (Recursive): {factorial_recursive(fact_num)}")
except ValueError:
    print("Invalid input. Please enter a valid non-negative integer for factorial.")

print("\n" + "="*30 + "\n") # Separator for clarity

# Exercise 9: Check for prime number
# This program takes an integer as input and checks if it is a prime number.
# A prime number is a natural number greater than 1 that has no positive divisors
# other than 1 and itself.
import math

def is_prime(num):
    if num <= 1:
        return False # Numbers less than or equal to 1 are not prime
    for i in range(2, int(math.sqrt(num)) + 1): # Check divisibility up to sqrt(num)
        if num % i == 0:
            return False # Found a divisor, so it's not prime
    return True # No divisors found, so it's prime

try:
    prime_num_str = input("Enter an integer to check if it's prime: ")
    prime_num = int(prime_num_str)

    if is_prime(prime_num):
        print(f"The number {prime_num} is a Prime number.")
    else:
        print(f"The number {prime_num} is NOT a Prime number.")
except ValueError:
    print("Invalid input. Please enter a valid integer for prime number check.")

print("\n" + "="*30 + "\n") # Separator for clarity

# Exercise 10: Simple calculator
# This program defines functions for basic arithmetic operations (add, subtract,
# multiply, divide) and allows the user to perform calculations.
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero!"
    return x / y

print("Simple Calculator")
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

try:
    choice = input("Enter choice(1/2/3/4): ")
    num1_calc_str = input("Enter first number: ")
    num2_calc_str = input("Enter second number: ")

    num1_calc = float(num1_calc_str)
    num2_calc = float(num2_calc_str)

    if choice == '1':
        print(f"{num1_calc} + {num2_calc} = {add(num1_calc, num2_calc)}")
    elif choice == '2':
        print(f"{num1_calc} - {num2_calc} = {subtract(num1_calc, num2_calc)}")
    elif choice == '3':
        print(f"{num1_calc} * {num2_calc} = {multiply(num1_calc, num2_calc)}")
    elif choice == '4':
        result = divide(num1_calc, num2_calc)
        print(f"{num1_calc} / {num2_calc} = {result}")
    else:
        print("Invalid Input")
except ValueError:
    print("Invalid input. Please enter valid numbers.")
except Exception as e:
    print(f"An error occurred: {e}")