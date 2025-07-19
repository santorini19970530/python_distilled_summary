"""
Book: Python Distilled
Author: David M. Beazley
Publisher: Pearson
ISBN: 978-0-13-417327-6
"""

# Chapter 1.11 - Dictionaries
# Dictionary Keys Example

d = {'x': 2, 'y': 3}

# Get the keys view
k = d.keys()
print(f"Initial keys: {k}")

# Add a new key
d['z'] = 4

# The keys view automatically reflects changes
print(f"Keys after adding 'z': {k}")

# The keys always appear in the same order as the items were
# initially inserted into the dictionary
print(f"All dictionary items: {d}")

# Convert keys to list if needed
keys_list = list(d.keys())
print(f"Keys as list: {keys_list}") 