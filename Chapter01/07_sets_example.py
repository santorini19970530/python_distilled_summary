"""
Book: Python Distilled
Author: David M. Beazley
Publisher: Pearson
ISBN: 978-0-13-417327-6
"""

# Chapter 1.10 - Sets
# Sets Example

# Creating a set from portfolio data
portfolio = [
    ('AA', 100, 32.2),
    ('IBM', 50, 91.1),
    ('CAT', 150, 83.44),
    ('MSFT', 200, 51.23),
    ('GE', 95, 40.37),
    ('MSFT', 50, 65.1),
    ('IBM', 100, 70.44)
]

# Extract unique company names
names = set()
for name, shares, price in portfolio:
    names.add(name)

print("Unique company names:")
print(names)

# Alternative way using set comprehension
names2 = {name for name, shares, price in portfolio}
print(f"\nNames using set comprehension: {names2}")

# Notice that 'IBM' only appears once in the set
# Also, the order of items can't be predicted 