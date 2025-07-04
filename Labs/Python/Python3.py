print("\n" + "="*30 + "\n") # Separator for clarity
print("--- Level 3: Working with Strings and Lists ---")

# Exercise 11: Count positive and negative numbers in a list
# This program takes a comma-separated string of numbers, converts it to a list,
# and then counts how many positive and negative numbers are present.
try:
    numbers_str_l3 = input("Enter a list of numbers separated by commas (e.g., 1,-2,3,0,-5): ")
    # Convert string input to a list of integers
    numbers_list_l3 = [int(num.strip()) for num in numbers_str_l3.split(',')]

    positive_count = 0
    negative_count = 0
    zero_count = 0 # Optional: count zeros as well

    for num in numbers_list_l3:
        if num > 0:
            positive_count += 1
        elif num < 0:
            negative_count += 1
        else:
            zero_count += 1

    print(f"In the list {numbers_list_l3}:")
    print(f"Number of positive numbers: {positive_count}")
    print(f"Number of negative numbers: {negative_count}")
    print(f"Number of zeros: {zero_count}")
except ValueError:
    print("Invalid input. Please enter numbers separated by commas.")
except Exception as e:
    print(f"An error occurred: {e}")

print("\n" + "="*30 + "\n") # Separator for clarity

# Exercise 12: Reverse a string
# This program demonstrates two ways to reverse a string:
# 1. Using string slicing (Pythonic and concise)
# 2. Using a loop
def reverse_string_slicing(s):
    return s[::-1] # [start:end:step], -1 step reverses the string

def reverse_string_loop(s):
    reversed_s = ""
    for char in s:
        reversed_s = char + reversed_s # Prepend each character
    return reversed_s

input_string_l3 = input("Enter a string to reverse: ")
print(f"Original string: '{input_string_l3}'")
print(f"Reversed string (slicing): '{reverse_string_slicing(input_string_l3)}'")
print(f"Reversed string (loop): '{reverse_string_loop(input_string_l3)}'")

print("\n" + "="*30 + "\n") # Separator for clarity

# Exercise 13: Count words in a sentence
# This program takes a sentence as input and counts the number of words in it.
# It splits the string by spaces and counts the resulting parts.
sentence_l3 = input("Enter a sentence to count its words: ")
# Split the sentence by spaces. .split() handles multiple spaces and leading/trailing spaces.
words_l3 = sentence_l3.split()
word_count_l3 = len(words_l3)
print(f"The sentence has {word_count_l3} words.")

print("\n" + "="*30 + "\n") # Separator for clarity

# Exercise 14: Find the second largest element in a list (without using sort())
# This program finds the second largest number in a list of numbers.
# It iterates through the list, keeping track of the largest and second largest.
try:
    numbers_str_l3_second_largest = input("Enter a list of numbers separated by commas (e.g., 10,5,20,15,25): ")
    numbers_list_l3_second_largest = [int(num.strip()) for num in numbers_str_l3_second_largest.split(',')]

    if len(numbers_list_l3_second_largest) < 2:
        print("List must contain at least two distinct numbers to find the second largest.")
    else:
        # Initialize largest and second_largest
        # Ensure they are distinct to handle cases like [5,5,5]
        largest = float('-inf') # Represents negative infinity
        second_largest = float('-inf')

        for num in numbers_list_l3_second_largest:
            if num > largest:
                second_largest = largest # Current largest becomes second largest
                largest = num           # New number is the largest
            elif num > second_largest and num != largest:
                second_largest = num    # New number is greater than second_largest but not largest

        if second_largest == float('-inf'):
            print("Could not find a distinct second largest number (e.g., all numbers are the same).")
        else:
            print(f"The second largest element in {numbers_list_l3_second_largest} is: {second_largest}")
except ValueError:
    print("Invalid input. Please enter numbers separated by commas.")
except Exception as e:
    print(f"An error occurred: {e}")

print("\n" + "="*30 + "\n") # Separator for clarity

# Exercise 15: Remove duplicate elements from a list
# This program takes a list and returns a new list with all duplicate elements removed.
# It demonstrates two common methods: using a set and using a loop with a new list.

# Method 1: Using a set (most Pythonic and efficient)
def remove_duplicates_set(input_list):
    return list(set(input_list)) # Convert to set (removes duplicates), then back to list

# Method 2: Using a loop and a new list
def remove_duplicates_loop(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

try:
    elements_str_l3_duplicates = input("Enter elements separated by commas (e.g., 1,2,2,3,1,4): ")
    # Convert string input to a list of strings (can be adapted for numbers if needed)
    elements_list_l3_duplicates = [item.strip() for item in elements_str_l3_duplicates.split(',')]

    print(f"Original list: {elements_list_l3_duplicates}")
    print(f"List after removing duplicates (using set): {remove_duplicates_set(elements_list_l3_duplicates)}")
    print(f"List after removing duplicates (using loop): {remove_duplicates_loop(elements_list_l3_duplicates)}")
except Exception as e:
    print(f"An error occurred: {e}")