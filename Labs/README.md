# python-tutorials
# 🐍 7-Day Python Learning Roadmap for Beginners

Welcome to your accelerated Python learning journey! This document is designed to help you, a complete beginner, grasp the fundamentals of Python within seven days, focusing on rapid learning and practical application.

Each day, you'll be introduced to a new set of concepts, accompanied by illustrative examples and a small project at the end to solidify your understanding.

---

## 📅 Day 1: Getting Started with Python Basics

**Content:**

- **Introduction to Python:** What Python is, why it's popular, and its ease of learning.
- **Installation and Development Environment (IDE):** Guide on installing Python and using VS Code or PyCharm.
- **Your First Python Program:** How to write and run a "Hello, World!" program.
- **Variables and Basic Data Types:**
  - Variables: Naming conventions and assigning values.
  - Data Types: `int`, `float`, `str`, `bool`.

**Example:**
```python
# Your first Python program
print("Hello, World!")

# Examples of variables and data types
name = "Alice"
age = 30
height = 1.65
is_student = False

print(f"Name: {name}, Age: {age}, Height: {height}, Is student: {is_student}")

# Check data types
print(type(name))
print(type(age))
print(type(height))
print(type(is_student))

```
---

## 📅 Day 2: Operators and Conditional Statements

**Content:**
- Arithmetic Operators: +, -, *, /, //, %, **
- Assignment Operators: =, +=, -=, etc.
- Comparison Operators: >, <, ==, !=, >=, <=
- Logical Operators: and, or, not
- Conditional Statements: if, elif, else

**Example:**
```python
# Arithmetic operators
a = 10
b = 3
print(f"Sum: {a + b}")
print(f"Difference: {a - b}")
print(f"Product: {a * b}")
print(f"Division: {a / b}")
print(f"Floor Division: {a // b}")
print(f"Modulo: {a % b}")
print(f"Exponentiation: {a ** b}")

# Conditional statements
score = 7.5
if score >= 9:
    print("Excellent!")
elif score >= 7:
    print("Good!")
elif score >= 5:
    print("Average.")
else:
    print("Needs improvement.")

```

## 📅 Day 3: Loops and Data Structures
**Content:**
- for Loop: Iterating with range(), strings, lists, tuples.
- while Loop: Repeat until a condition is false.
- break and continue: Control loop flow.
- Lists: Mutable ordered collections.
- Tuples: Immutable ordered collections.
- Dictionaries: Key-value pairs.

**Example:**
```python
# For loop
print("Numbers from 0 to 4:")
for i in range(5):
    print(i)

# While loop
count = 0
while count < 3:
    print(f"Count: {count}")
    count += 1

# List example
fruits = ["apple", "orange", "banana"]
print(f"Initial list: {fruits}")
fruits.append("mango")
print(f"List after adding: {fruits}")
print(f"Element at index 0: {fruits[0]}")
fruits.pop(1)
print(f"List after removing: {fruits}")

# Dictionary example
student = {
    "name": "Minh",
    "age": 16,
    "class": "10A"
}
print(f"Student name: {student['name']}")
student["math_score"] = 8.5
print(f"Student info: {student}")

```

## 📅 Day 4: Functions
**Content:**
- What Are Functions? Why we use them.
- Defining Functions: Using def.
- Parameters and Arguments
- Return Values
- Built-in Functions: len(), input(), type()

**Example:**
```python
# Simple function
def greet(name):
    print(f"Hello, {name}!")

greet("Khoa")
greet("Vy")

# Function with return value
def calculate_sum(num1, num2):
    return num1 + num2

result = calculate_sum(5, 7)
print(f"The sum of 5 and 7 is: {result}")

# Input function
user_name = input("Please enter your name: ")
print(f"Hello, {user_name}!")

```

## 📅 Day 5: Working with Strings and Input/Output
**Content:**
- String Concatenation
- String Formatting: f-strings, .format()
- Useful Methods: .upper(), .lower(), .strip(), .replace(), .split()
- Getting User Input: input()
- Printing Output: print()

**Example:**
```python
# String manipulation
string1 = "Python"
string2 = "is very interesting"
combined_string = string1 + " " + string2
print(f"Combined string: {combined_string}")

# f-string formatting
product = "Laptop"
price = 1200
print(f"Product: {product}, Price: ${price}")

# String methods
original_string = "   Hello Python!   "
print(f"Uppercase: {original_string.upper()}")
print(f"Lowercase: {original_string.lower()}")
print(f"Stripped: '{original_string.strip()}'")
print(f"Replaced: {original_string.replace('Python', 'World')}")

# Input and output
hobby = input("What is your hobby? ")
print(f"Oh, you like {hobby}. That's cool!")

```

## 📅 Day 6: Error Handling and Basic Modules
**Content:**
- try-except: Catching and handling exceptions.
- Modules: Using built-in modules like math, random, datetime.

**Example:**
```python
# Error handling
try:
    integer_input = int(input("Enter an integer: "))
    print(f"You entered: {integer_input}")
except ValueError:
    print("Error: This is not a valid integer.")

# Using modules
import math
import random
import datetime

print(f"Square root of 16: {math.sqrt(16)}")
print(f"Random number from 1 to 10: {random.randint(1, 10)}")
print(f"Current date: {datetime.date.today()}")

```

## 📅 Day 7: Small Practical Project
**Content:**
- Build a small app to apply everything learned.
- Ideas:
  - To-do List App
  - BMI Calculator
  - Number Guessing Game

**Example: Number Guessing Game**
```python
import random

def play_guessing_game():
    secret_number = random.randint(1, 20)
    guesses_taken = 0

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 20. Can you guess it?")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            guesses_taken += 1

            if guess < secret_number:
                print("Your guess is too low. Try again!")
            elif guess > secret_number:
                print("Your guess is too high. Try again!")
            else:
                print(f"Congratulations! You guessed the number {secret_number} in {guesses_taken} guesses.")
                break
        except ValueError:
            print("Please enter a valid integer.")

play_guessing_game()

```
