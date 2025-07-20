# Chapter 1: Python Basics

## 1. Running Python

[Hello World Example](Chapter01/01_hello_world.py)
[Calculator Example](Chapter01/02_calculator_example.py)

## 2. Python Programs

- Python programs are text files with `.py` extension
- Programs can be run from command line: `python filename.py`
- Python interpreter reads and executes code line by line
- Programs can be interactive (REPL) or script-based

### Program Structure

```python
#!/usr/bin/env python3  # Shebang line (Unix/Linux)
# -*- coding: utf-8 -*-  # Encoding declaration

# Import statements
import sys
import os

# Global variables
VERSION = "1.0"

# Function definitions
def main():
    print("Hello, World!")

# Main execution
if __name__ == "__main__":
    main()
```

## 3. Primitives, Variables, and Expressions

### Primitive Data Types

- **Numbers**: `int`, `float`, `complex`
- **Strings**: `str` (text data)
- **Booleans**: `True`, `False`
- **None**: `None` (null value)

### Variables

- Names that store values: `name = "Python"`
- Must start with letter or underscore
- Case-sensitive: `name` ≠ `Name`
- Can contain letters, digits, underscores

### Expressions

- Combinations of values, variables, and operators
- Evaluate to a single value
- Examples: `2 + 3`, `x * y`, `len("hello")`

[Interest Calculation](/Chapter01/03_interest.py)

## 4. Arithmetic Operators

### Basic Arithmetic Operators

| Symbol | Operation                         | Example Code              |
| ------ | --------------------------------- | ------------------------- |
| `+`    | Addition                          | `addition = a + b`        |
| `-`    | Subtraction                       | `subtraction = a - b`     |
| `*`    | Multiplicatio                     | `multiplication = a * b`  |
| `/`    | Division (returns float)          | `division = a / b`        |
| `//`   | Floor division (integer division) | `floor_division = a // b` |
| `%`    | Modulo (remainder)                | `modulo = a % b `         |
| `**`   | Exponentiation                    | `exponentiation = a ** b` |

(Working with different number types)

```python

int_division = 10 / 2 # 5.0 (always returns float)
int_floor = 10 // 3 # 3 (integer result)
float_math = 3.14 \* 2 # 6.28

# Negative numbers

negative = -5
absolute = abs(-5) # 5

```

Operator Precedence:

1. Parentheses `()`
2. Exponentiation `**`
3. Multiplication/Division `*`, `/`, `//`, `%`
4. Addition/Subtraction `+`, `-`

Precedence Examples:

```python
# Without parentheses (follows precedence)
result1 = 2 + 3 * 4     # 14 (3*4=12, then 2+12=14)

# With parentheses (overrides precedence)
result2 = (2 + 3) * 4   # 20 (2+3=5, then 5*4=20)

# Complex expressions
complex_expr = 2 ** 3 + 4 * 5 - 6 // 2
# 2**3=8, 4*5=20, 6//2=3, then 8+20-3=25
```

### Arithmetic Concepts

- **Type coercion**: Python automatically converts between number types
- **Integer division**: `//` always returns an integer
- **Float division**: `/` always returns a float
- **Modulo**: Returns remainder after division
- **Exponentiation**: `**` for power operations
- **Negative numbers**: Use `-` prefix
- **Absolute value**: Use `abs()` function

### Operator Reference Table

| Operator | Name           | Example       | Result | Notes                            |
| -------- | -------------- | ------------- | ------ | -------------------------------- |
| `+`      | Addition       | `5 + 3`       | `8`    | Works with numbers and strings   |
| `-`      | Subtraction    | `10 - 4`      | `6`    | Numbers only                     |
| `*`      | Multiplication | `3 * 7`       | `21`   | Works with numbers and sequences |
| `/`      | Division       | `15 / 3`      | `5.0`  | Always returns float             |
| `//`     | Floor Division | `15 // 4`     | `3`    | Integer result, rounds down      |
| `%`      | Modulo         | `17 % 5`      | `2`    | Remainder after division         |
| `**`     | Exponentiation | `2 ** 8`      | `256`  | Power operation                  |
| `()`     | Parentheses    | `(2 + 3) * 4` | `20`   | Override precedence              |

### Number Type Conversion Table

| Operation      | Input Types  | Result Type | Example           |
| -------------- | ------------ | ----------- | ----------------- |
| `int + int`    | `int, int`   | `int`       | `5 + 3 = 8`       |
| `int + float`  | `int, float` | `float`     | `5 + 3.0 = 8.0`   |
| `int / int`    | `int, int`   | `float`     | `10 / 2 = 5.0`    |
| `int // int`   | `int, int`   | `int`       | `10 // 3 = 3`     |
| `float ** int` | `float, int` | `float`     | `2.5 ** 2 = 6.25` |

### Common Arithmetic Functions

| Function       | Purpose                | Example             | Result   |
| -------------- | ---------------------- | ------------------- | -------- |
| `abs(x)`       | Absolute value         | `abs(-7)`           | `7`      |
| `round(x, n)`  | Round to n digits      | `round(3.14159, 2)` | `3.14`   |
| `divmod(x, y)` | Division and remainder | `divmod(17, 5)`     | `(3, 2)` |
| `pow(x, y)`    | Exponentiation         | `pow(2, 10)`        | `1024`   |
| `max(x, y, z)` | Maximum value          | `max(1, 5, 3)`      | `5`      |
| `min(x, y, z)` | Minimum value          | `min(1, 5, 3)`      | `1`      |

### Advanced Arithmetic Examples

```python
# Working with complex numbers
complex_num = 3 + 4j
magnitude = abs(complex_num)  # 5.0

# Rounding and precision
pi = 3.14159265359
rounded = round(pi, 3)        # 3.142
floor_rounded = round(pi)     # 3

# Division and remainder together
quotient, remainder = divmod(17, 5)  # (3, 2)

# Power operations
square = pow(5, 2)            # 25
cube = 5 ** 3                 # 125

# Finding extremes
numbers = [1, 5, 3, 9, 2, 7]
maximum = max(numbers)        # 9
minimum = min(numbers)        # 1
```

### Bit Manipulation Operators and Functions

Bit Operators

| Symbol | Operation   | Example Code      | Description                   |
| ------ | ----------- | ----------------- | ----------------------------- |
| `&`    | Bitwise AND | `result = a & b`  | Sets bit to 1 if both are 1   |
| `\|`   | Bitwise OR  | `result = a \| b` | Sets bit to 1 if either is 1  |
| `^`    | Bitwise XOR | `result = a ^ b`  | Sets bit to 1 if different    |
| `~`    | Bitwise NOT | `result = ~a`     | Inverts all bits              |
| `<<`   | Left shift  | `result = a << n` | Shifts bits left by n places  |
| `>>`   | Right shift | `result = a >> n` | Shifts bits right by n places |

Bit Manipulation Examples:

```python
# Basic bitwise operations
a, b = 5, 3  # 5 = 101, 3 = 011 in binary

# Bitwise AND
and_result = a & b      # 101 & 011 = 001 = 1

# Bitwise OR
or_result = a | b       # 101 | 011 = 111 = 7

# Bitwise XOR
xor_result = a ^ b      # 101 ^ 011 = 110 = 6

# Bitwise NOT
not_result = ~a         # ~101 = -6 (two's complement)

# Bit shifting
left_shift = a << 2     # 101 << 2 = 10100 = 20
right_shift = a >> 1    # 101 >> 1 = 10 = 2

# Practical examples
# Check if number is even/odd
is_even = (a & 1) == 0  # True if even, False if odd

# Multiply/divide by powers of 2
multiply_by_8 = a << 3  # a * 8
divide_by_4 = a >> 2    # a // 4

# Set specific bit
set_bit = a | (1 << 2)  # Set bit at position 2

# Clear specific bit
clear_bit = a & ~(1 << 0)  # Clear bit at position 0

# Toggle specific bit
toggle_bit = a ^ (1 << 1)  # Toggle bit at position 1
```

Bit Manipulation Functions:

```python
# Built-in functions for bit manipulation
bin_value = bin(42)         # '0b101010' - binary string
oct_value = oct(42)         # '0o52' - octal string
hex_value = hex(42)         # '0x2a' - hexadecimal string

# Count set bits
bit_count = bin(42).count('1')  # 3 (number of 1s in binary)

# Check if power of 2
def is_power_of_2(n):
    return n > 0 and (n & (n - 1)) == 0

# Get lowest set bit
lowest_bit = n & -n  # Gets the rightmost 1 bit
```

## 5. Conditionals and Control Flow

### Conditional Statements

```python
# if statement
if condition:
    # code block
elif another_condition:
    # code block
else:
    # code block

# Comparison operators
x == y    # Equal
x != y    # Not equal
x < y     # Less than
x > y     # Greater than
x <= y    # Less than or equal
x >= y    # Greater than or equal

# Logical operators
x and y   # Logical AND
x or y    # Logical OR
not x     # Logical NOT
```

### Control Flow

- **if/elif/else**: Conditional execution
- **pass**: Empty statement (placeholder)
- **Indentation**: Defines code blocks (4 spaces recommended)

## 6. Text Strings

### String Concepts

- **Immutable**: Strings cannot be changed after creation
- **Sequence**: Strings are sequences of characters
- **Indexed**: Access characters by position (0-based)
- **Slicing**: Extract substrings with slice notation

### String Operations

```python
# String creation
s1 = 'Hello'
s2 = "World"
s3 = '''Multi-line
string'''

print('''Content-type: text/html
<h1> Hello World </h1>
Click <a href="http://www.python.org">here</a>.
''')

# String concatenation
result = s1 + " " + s2  # "Hello World"

# String repetition
repeated = "Ha" * 3     # "HaHaHa"

# String length
length = len(s1)        # 5

# String indexing and slicing
first = s1[0]          # 'H'
last = s1[-1]          # 'o'
sub = s1[1:4]          # 'ell'
```

### Common String Methods

| Method         | Description                                | Example                     | Result            |
| -------------- | ------------------------------------------ | --------------------------- | ----------------- |
| `upper()`      | Convert to uppercase                       | `"hello".upper()`           | `"HELLO"`         |
| `lower()`      | Convert to lowercase                       | `"WORLD".lower()`           | `"world"`         |
| `title()`      | Title case (first letter of each word)     | `"hello world".title()`     | `"Hello World"`   |
| `capitalize()` | Capitalize first letter                    | `"hello".capitalize()`      | `"Hello"`         |
| `strip()`      | Remove whitespace from ends                | `"  hello  ".strip()`       | `"hello"`         |
| `lstrip()`     | Remove whitespace from left                | `"  hello".lstrip()`        | `"hello"`         |
| `rstrip()`     | Remove whitespace from right               | `"hello  ".rstrip()`        | `"hello"`         |
| `split()`      | Split into list by delimiter               | `"a,b,c".split(",")`        | `["a", "b", "c"]` |
| `join()`       | Join list into string                      | `"-".join(["a", "b", "c"])` | `"a-b-c"`         |
| `replace()`    | Replace substring                          | `"hello".replace("l", "x")` | `"hexxo"`         |
| `find()`       | Find substring (returns index)             | `"hello".find("ll")`        | `2`               |
| `index()`      | Find substring (raises error if not found) | `"hello".index("ll")`       | `2`               |
| `count()`      | Count occurrences                          | `"hello".count("l")`        | `2`               |
| `startswith()` | Check if starts with                       | `"hello".startswith("he")`  | `True`            |
| `endswith()`   | Check if ends with                         | `"hello".endswith("lo")`    | `True`            |
| `isalpha()`    | Check if all alphabetic                    | `"hello".isalpha()`         | `True`            |
| `isdigit()`    | Check if all digits                        | `"123".isdigit()`           | `True`            |
| `isalnum()`    | Check if alphanumeric                      | `"hello123".isalnum()`      | `True`            |
| `isspace()`    | Check if all whitespace                    | `"   ".isspace()`           | `True`            |

### String Formatting Methods

| Method       | Description               | Example                        | Result            |
| ------------ | ------------------------- | ------------------------------ | ----------------- |
| `format()`   | Format with placeholders  | `"Hello, {}!".format("Alice")` | `"Hello, Alice!"` |
| f-strings    | Formatted string literals | `f"Hello, {name}!"`            | `"Hello, Alice!"` |
| `%` operator | Old-style formatting      | `"Hello, %s!" % "Alice"`       | `"Hello, Alice!"` |

[String Representation Examples](Chapter01/04_string_representation.py)
[Formatting Examples](Chapter01/05_formatting_example.py)

## 7. File Input and Output

### File Operations

```python
# Reading files
with open('filename.txt', 'r') as file:
    content = file.read()        # Read entire file
    lines = file.readlines()     # Read as list of lines
    for line in file:            # Read line by line
        print(line.strip())

# Writing files
with open('output.txt', 'w') as file:
    file.write("Hello, World!")  # Write string
    file.writelines(lines)       # Write list of strings

# File modes
'r'   # Read (default)
'w'   # Write (overwrites)
'a'   # Append
'r+'  # Read and write
'b'   # Binary mode
```

- **Context managers** (`with` statement) automatically close files
- **File objects** are iterable (can use in for loops)
- **Encoding**: Specify encoding for text files: `open('file.txt', 'r', encoding='utf-8')`

## 8. Lists

### List Concepts

- **Mutable**: Lists can be modified after creation
- **Ordered**: Elements maintain their order
- **Indexed**: Access elements by position (0-based)
- **Heterogeneous**: Can contain different data types
- **Dynamic**: Can grow or shrink in size

### List Operations

```python
# Creating lists
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]
empty = []

# List indexing and slicing
first = numbers[0]      # 1
last = numbers[-1]      # 5
subset = numbers[1:4]   # [2, 3, 4]

# List concatenation
combined = numbers + [6, 7]  # [1, 2, 3, 4, 5, 6, 7]

# List repetition
repeated = [1, 2] * 3   # [1, 2, 1, 2, 1, 2]
```

[Portfolio Example](Chapter01/06_portfolio_example.py)

### List Methods

- `append(x)` - Add item to end
- `extend(iterable)` - Add all items from iterable
- `insert(i, x)` - Insert item at position i
- `remove(x)` - Remove first occurrence of x
- `pop([i])` - Remove and return item at position i
- `clear()` - Remove all items
- `index(x)` - Return index of first occurrence of x
- `count(x)` - Return number of occurrences of x
- `sort()` - Sort items in place
- `reverse()` - Reverse items in place

## 9. Tuples

### Tuple Characteristics

- **Immutable**: Cannot be changed after creation
- **Ordered**: Elements maintain their order
- **Indexed**: Access elements by position
- **Heterogeneous**: Can contain different data types

### Tuple Operations

```python
# Creating tuples
point = (10, 20)
coordinates = (x, y, z)
singleton = (42,)  # Note the comma

# Accessing elements
x = point[0]       # 10
y = point[1]       # 20

# Tuple unpacking
x, y = point
a, b, c = coordinates

# Tuple methods
point.count(10)    # Count occurrences
point.index(20)    # Find index of element
```

### Use Cases

- **Return multiple values** from functions
- **Data that shouldn't change** (coordinates, dates)
- **Dictionary keys** (tuples are hashable)
- **Named tuples** for structured data

## 10. Sets

### Set Concepts

- **Mutable**: Sets can be modified after creation
- **Unordered**: Elements have no specific order
- **Unique**: No duplicate elements allowed
- **Unindexed**: Cannot access elements by position
- **Hashable elements**: Elements must be immutable

### Set Operations

```python
# Creating sets
numbers = {1, 2, 3, 4, 5}
fruits = set(['apple', 'banana', 'orange'])
empty = set()

# Set operations
numbers.add(6)           # Add element
numbers.remove(1)        # Remove element (raises KeyError if not found)
numbers.discard(10)      # Remove element (no error if not found)

# Set operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
union = set1 | set2              # {1, 2, 3, 4, 5, 6}
intersection = set1 & set2       # {3, 4}
difference = set1 - set2         # {1, 2}
symmetric_diff = set1 ^ set2     # {1, 2, 5, 6}
```

[Sets Example](Chapter01/07_sets_example.py)

### Set Methods

- `add(elem)` - Add element
- `remove(elem)` - Remove element (raises KeyError)
- `discard(elem)` - Remove element (no error)
- `pop()` - Remove and return arbitrary element
- `clear()` - Remove all elements
- `union(other)` - Return union of sets
- `intersection(other)` - Return intersection
- `difference(other)` - Return difference
- `symmetric_difference(other)` - Return symmetric difference

## 11. Dictionaries

### Dictionary Concepts

- **Mutable**: Dictionaries can be modified after creation
- **Key-value pairs**: Store data as key-value associations
- **Unordered**: Key-value pairs have no specific order (Python 3.7+ preserves insertion order)
- **Keys must be hashable**: Keys must be immutable (strings, numbers, tuples)
- **Values can be anything**: Values can be any Python object

### Dictionary Operations

```python
# Creating dictionaries
prices = {'GOOG': 490.10, 'AAPL': 145.30, 'MSFT': 300.50}
empty = {}
mixed = {1: 'one', 'two': 2, (1, 2): 'tuple_key'}

# Accessing values
goog_price = prices['GOOG']
aapl_price = prices.get('AAPL', 0)  # With default value

# Modifying dictionaries
prices['TSLA'] = 250.00    # Add new key-value pair
prices['GOOG'] = 495.20    # Update existing value
del prices['MSFT']         # Remove key-value pair

# Dictionary methods
keys = list(prices.keys())     # Get all keys
values = list(prices.values()) # Get all values
items = list(prices.items())   # Get all key-value pairs
```

[Dictionary Keys Example](Chapter01/08_dictionary_keys_example.py)

### Dictionary Methods

- `get(key[, default])` - Get value with optional default
- `setdefault(key[, default])` - Get value, set default if key doesn't exist
- `update([other])` - Update dict with key-value pairs
- `pop(key[, default])` - Remove key and return value
- `popitem()` - Remove and return (key, value) pair
- `clear()` - Remove all items
- `keys()` - Return view of keys
- `values()` - Return view of values
- `items()` - Return view of (key, value) pairs

## 12. Iteration and Looping

### Loop Types

```python
# for loop with range
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# for loop with sequence
for item in [1, 2, 3, 4, 5]:
    print(item)

# for loop with enumerate
for index, value in enumerate(['a', 'b', 'c']):
    print(f"{index}: {value}")

# while loop
count = 0
while count < 5:
    print(count)
    count += 1

# Loop control
for i in range(10):
    if i == 5:
        break      # Exit loop
    if i == 2:
        continue   # Skip iteration
```

### Iteration Concepts

- **Iterables**: Objects that can be looped over (lists, strings, files)
- **Iterators**: Objects that produce values one at a time
- **Generator expressions**: Memory-efficient iteration: `(x**2 for x in range(5))`

### List Comprehensions

```python
# Basic list comprehension
squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]

# List comprehension with condition
evens = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]

# Nested list comprehension
matrix = [[i+j for j in range(3)] for i in range(3)]
# [[0, 1, 2], [1, 2, 3], [2, 3, 4]]
```

## 13. Functions

### Function Definition

```python
def greet(name, greeting="Hello"):
    # Return a greeting message.
    return f"{greeting}, {name}!"

# Function calls
message = greet("Alice")           # "Hello, Alice!"
custom = greet("Bob", "Hi")        # "Hi, Bob!"

# Function can return tuple which includes multiple values

def divide(a, b):
    q = a // b integer
    r = a - q * b
    return (q, r)

quotient, remainder = divide(1456, 33)

# Lambda functions
square = lambda x: x**2
result = square(5)  # 25
```

### Function Concepts

- **Parameters**: Input values (positional, keyword, default)
- **Return values**: Output from function
- **Scope**: Variable visibility (local vs global)
- **Docstrings**: Documentation strings (`"""..."""`)
- **Lambda functions**: Anonymous one-line functions

### Function Types

```python
# Function with default arguments
def power(base, exponent=2):
    return base ** exponent

# Function with variable arguments
def sum_all(*args):
    return sum(args)

# Function with keyword arguments
def create_profile(name, **kwargs):
    profile = {'name': name}
    profile.update(kwargs)
    return profile
```

## 14. Exceptions

### Exception Handling

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
except Exception as e:
    print(f"An error occurred: {e}")
else:
    print("No exception occurred")
finally:
    print("This always executes")
```

### Exception Concepts

- **try/except**: Catch and handle errors
- **Exception hierarchy**: Specific exceptions before general ones
- **else clause**: Executes if no exception occurs
- **finally clause**: Always executes (cleanup code)
- **raise**: Manually raise exceptions
- **Custom exceptions**: Define your own exception classes

### Exception Types

```python
# Common built-in exceptions
ValueError        # Invalid value
TypeError         # Invalid type
IndexError        # Invalid index
KeyError          # Invalid dictionary key
FileNotFoundError # File not found
AttributeError    # Invalid attribute

# Custom exceptions
class CustomError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
```

## 15. Python Termination

### Program Termination

```python
# Normal termination
exit()           # Exit with status 0
sys.exit(0)      # Exit with status 0
sys.exit(1)      # Exit with error status

# Force termination
os._exit(0)      # Immediate termination (bypass cleanup)

# Cleanup on exit
import atexit
atexit.register(cleanup_function)
```

### Termination Concepts

- **Normal exit**: Program completes successfully
- **Error exit**: Program exits due to error
- **Exit codes**: 0 = success, non-zero = error
- **Cleanup**: Finalization code runs before exit
- **Signal handling**: Respond to system signals

## 16. Objects and Classes

### Object-Oriented Programming Concepts

- **Objects**: Instances of classes that contain data and behavior
- **Classes**: Blueprints for creating objects
- **Encapsulation**: Bundling data and methods that operate on that data
- **Inheritance**: Creating new classes based on existing ones
- **Polymorphism**: Different classes can have methods with the same name
- **Abstraction**: Hiding complex implementation details

### Class Structure

```python
class Person:
    """A simple person class."""

    def __init__(self, name, age):
        self.name = name  # Instance variable
        self.age = age

    def greet(self):
        return f"Hello, I'm {self.name}"

    def have_birthday(self):
        self.age += 1
        return f"Happy birthday! I'm now {self.age}"

# Creating objects
person = Person("Alice", 30)
print(person.greet())  # "Hello, I'm Alice"
```

[dir() Function Example](Chapter01/09_dir_function_example.py)
[Stack Class Example](Chapter01/10_stack_class.py)
[Inheritance Example](Chapter01/11_inheritance_example.py)
[Calculator Example](Chapter01/12_calculator_example.py)

## 17. Modules

### Module Import Syntax

```python
import math                    # Import entire module
from math import sqrt, pi      # Import specific items
import math as m              # Import with alias
from math import *            # Import all (not recommended)
```

### Module Concepts

- **Modules**: Python files that can be imported
- **Packages**: Directories containing modules
- **Namespace**: Scope for names (variables, functions, classes)
- **`__name__`**: Special variable (`"__main__"` when run directly)
- **`__init__.py`**: Makes directory a package
- **Relative imports**: Import from same package

### Module Usage

```python
# Creating a module (my_module.py)
def greet(name):
    return f"Hello, {name}!"

PI = 3.14159

# Using the module
import my_module
print(my_module.greet("Alice"))  # "Hello, Alice!"
print(my_module.PI)              # 3.14159

# Import specific items
from my_module import greet, PI
print(greet("Bob"))              # "Hello, Bob!"
```

## 18. Script Writing

### Script Structure

```python
#!/usr/bin/env python3
"""
Script description and usage.
"""

import sys
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description='Script description')
    parser.add_argument('input', help='Input file')
    parser.add_argument('-o', '--output', help='Output file')
    return parser.parse_args()

def main():
    args = parse_arguments()
    # Main script logic here
    print(f"Processing {args.input}")

if __name__ == "__main__":
    main()
```

### Script Best Practices

- **Shebang line**: `#!/usr/bin/env python3`
- **Docstring**: Document purpose and usage
- **Argument parsing**: Use `argparse` for command-line arguments
- **Main function**: Separate main logic from imports
- **Error handling**: Graceful error messages
- **Exit codes**: Return appropriate exit status

## 19. Packages

### Package Structure

```
mypackage/
├── __init__.py          # Makes directory a package
├── module1.py           # Package modules
├── module2.py
├── subpackage/          # Subpackage
│   ├── __init__.py
│   └── submodule.py
└── setup.py             # Package metadata
```

### Package Concepts

- **`__init__.py`**: Required file to make directory a package
- **Namespace packages**: Packages without `__init__.py`
- **Relative imports**: `from . import module`
- **Package hierarchy**: Organize related modules
- **Distribution**: Share packages via PyPI
- **Virtual environments**: Isolate package dependencies

## 20. Structuring an Application

### Application Structure

```
myapp/
├── myapp/               # Main package
│   ├── __init__.py
│   ├── main.py          # Entry point
│   ├── models.py        # Data models
│   ├── views.py         # User interface
│   └── utils.py         # Utility functions
├── tests/               # Test suite
│   ├── __init__.py
│   └── test_main.py
├── docs/                # Documentation
├── requirements.txt     # Dependencies
├── setup.py            # Package setup
└── README.md           # Project description
```

### Application Design Principles

- **Separation of concerns**: Different modules for different responsibilities
- **Single responsibility**: Each module has one clear purpose
- **Dependency management**: Clear import structure
- **Configuration**: Separate config from code
- **Testing**: Include comprehensive tests
- **Documentation**: Clear documentation for users and developers

## 21. Managing Third-Party Packages

### Package Management

```bash
# Install packages
pip install package_name
pip install -r requirements.txt

# Virtual environments
python -m venv myenv
source myenv/bin/activate  # Unix/Linux
myenv\Scripts\activate     # Windows

# Package management tools
pip install --upgrade pip
pip list                   # List installed packages
pip show package_name      # Show package info
pip freeze > requirements.txt  # Save dependencies
```

### Package Management Concepts

- **pip**: Python package installer
- **Virtual environments**: Isolated Python environments
- **requirements.txt**: List of package dependencies
- **PyPI**: Python Package Index (package repository)
- **Version pinning**: Specify exact package versions
- **Dependency resolution**: Automatic dependency management

## 22. Python: It Fits Your Brain

### Python Philosophy

- **Readability**: Code should be easy to read and understand
- **Explicit over implicit**: Clear is better than clever
- **Simple over complex**: Simple solutions are preferred
- **Practicality**: Practicality beats purity

### Python Design Principles

- **The Zen of Python**: `import this` reveals Python's philosophy
- **Batteries included**: Rich standard library
- **Cross-platform**: Works on multiple operating systems
- **Community-driven**: Open source with active community
- **Learning curve**: Gentle learning curve for beginners
- **Versatility**: Suitable for many domains (web, data, AI, etc.)

### Key Strengths

- **Rapid development**: Quick prototyping and development
- **Large ecosystem**: Extensive third-party packages
- **Integration**: Easy integration with other languages
- **Documentation**: Excellent documentation and tutorials
