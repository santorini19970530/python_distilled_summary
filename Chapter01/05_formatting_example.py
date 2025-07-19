"""
Book: Python Distilled
Author: David M. Beazley
Publisher: Pearson
ISBN: 978-0-13-417327-6
"""

# Chapter 1.6 - Text Strings
# Formatting Examples

x = 12.34567

# Using format() function
formatted1 = format(x, '0.2f')
print(f"format(x, '0.2f'): {formatted1}")

# Using f-strings (preferred method)
formatted2 = f'{x:0.2f}'
print(f"f'{{x:0.2f}}': {formatted2}")

# The format code given to format() is the same code you would
# use with f-strings when producing formatted output 
