Here's a comprehensive Python cheat sheet, designed for quick reference. It covers fundamental concepts, syntax, and common operations.

-----

## 🐍 Python Cheat Sheet: Quick Reference Guide

### 1\. Basic Syntax & Output

  * **Print to console:**
    ```python
    print("Hello, World!")
    ```
  * **Comments:**
    ```python
    # This is a single-line comment

    """
    This is a
    multi-line comment
    or docstring.
    """
    ```

### 2\. Variables & Data Types

  * **Assignment:**
    ```python
    my_integer = 10
    my_float = 3.14
    my_string = "Hello"
    my_boolean = True # or False
    my_none = None # Represents absence of a value
    ```
  * **Checking type:**
    ```python
    print(type(my_integer)) # <class 'int'>
    ```

### 3\. Operators

  * **Arithmetic:** `+`, `-`, `*`, `/`, `%` (modulo), `**` (exponent), `//` (floor division)
  * **Comparison:** `==` (equal to), `!=` (not equal to), `>` (greater than), `<` (less than), `>=` (greater than or equal to), `<=` (less than or equal to)
  * **Logical:** `and`, `or`, `not`
  * **Assignment:** `=`, `+=`, `-=`, `*=`, `/=`, `%=`, `**=`, `//=`
  * **Identity:** `is`, `is not` (checks if two variables refer to the same object)
  * **Membership:** `in`, `not in` (checks if a value is present in a sequence)

### 4\. Strings

  * **Creation:**
    ```python
    s1 = "Hello"
    s2 = 'World'
    s3 = """Multi-line
    string"""
    ```
  * **Concatenation:**
    ```python
    full_name = "John" + " " + "Doe" # "John Doe"
    ```
  * **F-strings (formatted string literals - Python 3.6+):**
    ```python
    name = "Alice"
    age = 30
    message = f"My name is {name} and I am {age} years old."
    ```
  * **Common Methods:**
    ```python
    "hello".upper()        # 'HELLO'
    "HELLO".lower()        # 'hello'
    "  hello  ".strip()    # 'hello' (removes whitespace)
    "Hello World".replace("World", "Python") # 'Hello Python'
    "apple,banana".split(",") # ['apple', 'banana']
    "Python".startswith("Py") # True
    "Python".endswith("on")   # True
    "hello".find("lo")        # 3 (index of first occurrence)
    "hello".count("l")        # 2
    len("hello")             # 5 (length of string)
    ```

### 5\. Lists (Mutable, Ordered Sequences)

  * **Creation:**
    ```python
    my_list = [1, 2, 3, "four"]
    empty_list = []
    ```
  * **Access elements:**
    ```python
    my_list[0]    # 1 (first element)
    my_list[-1]   # "four" (last element)
    my_list[1:3]  # [2, 3] (slice from index 1 up to (but not including) 3)
    my_list[:2]   # [1, 2] (slice from beginning to index 2)
    my_list[2:]   # [3, 'four'] (slice from index 2 to end)
    ```
  * **Common Methods:**
    ```python
    my_list.append(5)      # [1, 2, 3, "four", 5]
    my_list.insert(1, 0)   # [1, 0, 2, 3, "four", 5]
    my_list.pop()          # Removes and returns last item (5)
    my_list.remove(2)      # Removes the first occurrence of 2
    my_list.sort()         # Sorts in-place (if elements are comparable)
    my_list.reverse()      # Reverses in-place
    len(my_list)           # Length of the list
    2 in my_list           # True (membership check)
    ```

### 6\. Tuples (Immutable, Ordered Sequences)

  * **Creation:**
    ```python
    my_tuple = (1, 2, "three")
    single_item_tuple = (5,) # Comma is crucial!
    ```
  * **Access:** Same as lists (indexing, slicing).
  * **Immutable:** Cannot change elements after creation.

### 7\. Dictionaries (Mutable, Unordered Key-Value Pairs)

  * **Creation:**
    ```python
    my_dict = {"name": "Alice", "age": 30, "city": "New York"}
    empty_dict = {}
    ```
  * **Access elements:**
    ```python
    my_dict["name"] # 'Alice'
    my_dict.get("age") # 30 (safer, returns None if key not found)
    ```
  * **Add/Update:**
    ```python
    my_dict["email"] = "alice@example.com"
    my_dict["age"] = 31 # Updates existing value
    ```
  * **Common Methods:**
    ```python
    my_dict.keys()   # dict_keys(['name', 'age', 'city', 'email'])
    my_dict.values() # dict_values(['Alice', 31, 'New York', 'alice@example.com'])
    my_dict.items()  # dict_items([('name', 'Alice'), ...])
    my_dict.pop("city") # Removes 'city' and returns its value
    len(my_dict)     # Length of the dictionary
    "name" in my_dict # True (key membership check)
    ```

### 8\. Sets (Mutable, Unordered Collections of Unique Elements)

  * **Creation:**
    ```python
    my_set = {1, 2, 3, 2} # {1, 2, 3} (duplicates are removed)
    empty_set = set()
    ```
  * **Common Methods:**
    ```python
    my_set.add(4)        # {1, 2, 3, 4}
    my_set.remove(2)     # {1, 3, 4}
    set1.union(set2)     # Combines elements from both
    set1.intersection(set2) # Elements common to both
    set1.difference(set2)  # Elements in set1 but not set2
    len(my_set)
    ```

### 9\. Control Flow

  * **`if`/`elif`/`else`:**
    ```python
    x = 10
    if x > 10:
        print("x is greater than 10")
    elif x == 10:
        print("x is 10")
    else:
        print("x is less than 10")
    ```
  * **Ternary Operator (Conditional Expression):**
    ```python
    status = "Even" if x % 2 == 0 else "Odd"
    ```

### 10\. Loops

  * **`for` loop (Iterating over sequences):**
    ```python
    for item in [1, 2, 3]:
        print(item)

    for i in range(5): # 0, 1, 2, 3, 4
        print(i)

    for key, value in my_dict.items():
        print(f"{key}: {value}")
    ```
  * **`while` loop:**
    ```python
    count = 0
    while count < 3:
        print(count)
        count += 1
    ```
  * **Loop control:**
      * `break`: Exits the loop entirely.
      * `continue`: Skips the rest of the current iteration and goes to the next.

### 11\. Functions

  * **Define a function:**
    ```python
    def greet(name):
        return f"Hello, {name}!"

    def add(a, b=0): # b has a default value
        return a + b
    ```
  * **Call a function:**
    ```python
    message = greet("Bob") # "Hello, Bob!"
    sum_val = add(5, 3)    # 8
    sum_val_default = add(7) # 7 (b uses default 0)
    ```
  * **Arbitrary Arguments (`*args`, `**kwargs`):**
    ```python
    def my_sum(*args): # Accepts any number of positional arguments as a tuple
        return sum(args)

    def print_info(**kwargs): # Accepts any number of keyword arguments as a dictionary
        for key, value in kwargs.items():
            print(f"{key}: {value}")

    my_sum(1, 2, 3) # 6
    print_info(name="Carol", age=25)
    ```

### 12\. Classes & Objects (OOP)

  * **Define a class:**
    ```python
    class Dog:
        # Class attribute (shared by all instances)
        species = "Canis familiaris"

        # Constructor
        def __init__(self, name, breed):
            self.name = name # Instance attribute
            self.breed = breed

        # Instance method
        def bark(self):
            return f"{self.name} says Woof!"

        # String representation for the object
        def __str__(self):
            return f"{self.name} ({self.breed})"
    ```
  * **Create an object (instance):**
    ```python
    my_dog = Dog("Buddy", "Golden Retriever")
    ```
  * **Access attributes/methods:**
    ```python
    print(my_dog.name)        # "Buddy"
    print(my_dog.species)     # "Canis familiaris"
    print(my_dog.bark())      # "Buddy says Woof!"
    print(my_dog)             # "Buddy (Golden Retriever)"
    ```
  * **Inheritance:**
    ```python
    class Labrador(Dog):
        def __init__(self, name, color):
            super().__init__(name, "Labrador") # Call parent constructor
            self.color = color

        def retrieve(self):
            return f"{self.name} is retrieving."
    ```

### 13\. Error Handling

  * **`try`/`except`/`finally`:**
    ```python
    try:
        result = 10 / 0
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    except TypeError as e: # Catch specific error and alias it
        print(f"Type error: {e}")
    else: # Optional: runs if no exception occurred in try block
        print("Division successful.")
    finally: # Optional: always runs, regardless of exception
        print("Execution finished.")
    ```
  * **Raising exceptions:**
    ```python
    raise ValueError("Invalid value provided.")
    ```

### 14\. File I/O (Input/Output)

  * **Writing to a file:**
    ```python
    with open("my_file.txt", "w") as f: # 'w' for write (creates/overwrites)
        f.write("Hello, Python!\n")
        f.write("This is a new line.")
    ```
  * **Reading from a file:**
    ```python
    with open("my_file.txt", "r") as f: # 'r' for read
        content = f.read() # Reads entire file
        print(content)

    with open("my_file.txt", "r") as f:
        for line in f: # Reads line by line
            print(line.strip()) # .strip() removes newline character
    ```
  * **Append to a file:**
    ```python
    with open("my_file.txt", "a") as f: # 'a' for append
        f.write("\nAppending more text.")
    ```

### 15\. Modules & Packages

  * **Import a module:**
    ```python
    import math
    print(math.sqrt(16)) # 4.0
    ```
  * **Import specific items:**
    ```python
    from datetime import date
    today = date.today()
    print(today)
    ```
  * **Import with an alias:**
    ```python
    import numpy as np
    ```

-----

This cheat sheet should serve as a helpful quick reference for your Python journey. Python's versatility means there's always more to learn, but these fundamentals will get you far\!

Do you have any specific areas of Python you'd like to explore in more detail?