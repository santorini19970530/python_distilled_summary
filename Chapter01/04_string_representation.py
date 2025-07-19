"""
Book: Python Distilled
Author: David M. Beazley
Publisher: Pearson
ISBN: 978-0-13-417327-6
"""

# Chapter 1.6 - Text Strings
# String Representation Examples

s = 'hello\nworld'

# str() produces a string representation suitable for display
print("str(s):")
print(str(s))

# repr() produces a string representation that can be used to recreate the object
print("\nrepr(s):")
print(repr(s))

# When debugging, use repr(s) to produce output because it
# shows you more information about a value and its type 
