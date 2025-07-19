"""
Book: Python Distilled
Author: David M. Beazley
Publisher: Pearson
ISBN: 978-0-13-417327-6
"""

# Chapter 1.16 - Objects and Classes
# dir() Function Example

items = [37, 42]

# dir() is a useful tool for interactive experimentation
# It lists all attributes and methods of an object
print("Available methods and attributes:")
print(dir(items))

# You can see familiar methods like append, count, extend, etc.
print(f"\nCan append: {'append' in dir(items)}")
print(f"Can extend: {'extend' in dir(items)}")
print(f"Can pop: {'pop' in dir(items)}")

# You can also see special methods that implement operators
print(f"\nHas __add__ method: {'__add__' in dir(items)}")

# These methods implement various operators
# For example, __add__() is used to implement the + operator
result = items.__add__([73, 101])
print(f"Using __add__ method: {result}")

# This is equivalent to:
result2 = items + [73, 101]
print(f"Using + operator: {result2}") 