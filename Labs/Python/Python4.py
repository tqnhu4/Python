print("\n" + "="*30 + "\n") # Separator for clarity
print("--- Level 4: Working with Dictionaries, Tuples, Files ---")

# Exercise 16: Character frequency in a string
# This program takes a string as input and returns a dictionary
# where keys are characters and values are their frequencies.
def count_char_frequency(input_string):
    frequency = {}
    for char in input_string:
        frequency[char] = frequency.get(char, 0) + 1
    return frequency

input_string_l4_freq = input("Enter a string to count character frequencies: ")
char_freq_result = count_char_frequency(input_string_l4_freq)
print(f"Character frequencies: {char_freq_result}")

print("\n" + "="*30 + "\n") # Separator for clarity

# Exercise 17: Merge two dictionaries
# This program merges two dictionaries. If a key exists in both, their values are added.
def merge_dictionaries(dict1, dict2):
    merged_dict = dict1.copy() # Start with a copy of the first dictionary
    for key, value in dict2.items():
        if key in merged_dict:
            merged_dict[key] += value # Add values if key exists
        else:
            merged_dict[key] = value # Otherwise, add the new key-value pair
    return merged_dict

# Example dictionaries
dict_a = {'a': 10, 'b': 20, 'c': 30}
dict_b = {'b': 5, 'c': 15, 'd': 25}
print(f"Dictionary A: {dict_a}")
print(f"Dictionary B: {dict_b}")
merged_result = merge_dictionaries(dict_a, dict_b)
print(f"Merged dictionary: {merged_result}")

print("\n" + "="*30 + "\n") # Separator for clarity

# Exercise 18: Write/read text file
# This program demonstrates how to write content to a text file
# and then read its content back.
file_name = "sample.txt"
content_to_write = "This is a sample line.\nAnother line of text.\nEnd of file."

# Writing to a file
try:
    with open(file_name, 'w') as file: # 'w' for write mode (creates/overwrites file)
        file.write(content_to_write)
    print(f"Content successfully written to '{file_name}'")
except IOError as e:
    print(f"Error writing to file: {e}")

# Reading from a file
try:
    with open(file_name, 'r') as file: # 'r' for read mode
        read_content = file.read()
    print(f"\nContent read from '{file_name}':")
    print(read_content)
except FileNotFoundError:
    print(f"Error: The file '{file_name}' was not found.")
except IOError as e:
    print(f"Error reading from file: {e}")

print("\n" + "="*30 + "\n") # Separator for clarity

# Exercise 19: Create a functional menu
# This program creates a simple text-based menu that allows the user
# to choose between calculating sum, checking for prime numbers, or exiting.

# Re-using functions from Level 2
def add_l4(x, y):
    return x + y

def is_prime_l4(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def display_menu():
    print("\n--- Menu ---")
    print("1. Calculate Sum of Two Numbers")
    print("2. Check if a Number is Prime")
    print("3. Exit")
    print("------------")

def run_menu():
    while True:
        display_menu()
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                print(f"Sum: {add_l4(num1, num2)}")
            except ValueError:
                print("Invalid input. Please enter valid numbers.")
        elif choice == '2':
            try:
                num = int(input("Enter an integer to check for prime: "))
                if is_prime_l4(num):
                    print(f"{num} is a Prime number.")
                else:
                    print(f"{num} is NOT a Prime number.")
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
        elif choice == '3':
            print("Exiting the menu. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

# Uncomment the line below to run the menu
# run_menu()
print("To run the menu, uncomment 'run_menu()' at the end of Exercise 19.")

print("\n" + "="*30 + "\n") # Separator for clarity

# Exercise 20: Simple contact management
# This program implements a basic contact management system using a dictionary.
# Users can add, delete, and find phone numbers.
contacts = {}

def add_contact(name, phone_number):
    contacts[name.lower()] = phone_number # Store names in lowercase for case-insensitive lookup
    print(f"Contact '{name}' added/updated.")

def delete_contact(name):
    if name.lower() in contacts:
        del contacts[name.lower()]
        print(f"Contact '{name}' deleted.")
    else:
        print(f"Contact '{name}' not found.")

def find_contact(name):
    if name.lower() in contacts:
        print(f"Phone number for '{name}': {contacts[name.lower()]}")
    else:
        print(f"Contact '{name}' not found.")

def display_contacts():
    if not contacts:
        print("No contacts available.")
    else:
        print("\n--- Your Contacts ---")
        for name, number in contacts.items():
            print(f"{name.capitalize()}: {number}") # Capitalize for display
        print("---------------------")

# Example usage of contact management
print("--- Simple Contact Management ---")
add_contact("Alice", "123-456-7890")
add_contact("Bob", "987-654-3210")
display_contacts()

find_contact("Alice")
find_contact("Charlie")

delete_contact("Bob")
display_contacts()

# You can also add an interactive loop for contact management similar to the menu.
# For example:
# while True:
#     print("\nContact Menu:")
#     print("1. Add Contact")
#     print("2. Delete Contact")
#     print("3. Find Contact")
#     print("4. Display All Contacts")
#     print("5. Exit")
#     choice = input("Enter your choice: ")
#     if choice == '1':
#         name = input("Enter contact name: ")
#         number = input("Enter phone number: ")
#         add_contact(name, number)
#     elif choice == '2':
#         name = input("Enter name to delete: ")
#         delete_contact(name)
#     elif choice == '3':
#         name = input("Enter name to find: ")
#         find_contact(name)
#     elif choice == '4':
#         display_contacts()
#     elif choice == '5':
#         break
#     else:
#         print("Invalid choice.")