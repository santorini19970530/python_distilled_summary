"""
Book: Python Distilled
Author: David M. Beazley
Publisher: Pearson
ISBN: 978-0-13-417327-6
"""

# Chapter 1.16 - Objects and Classes
# Stack Class Example

class Stack:
    def __init__(self):
        self._items = []
    
    def push(self, item):
        self._items.append(item)
    
    def pop(self):
        return self._items.pop()
    
    def __len__(self):
        return len(self._items)
    
    def __repr__(self):
        return f"<Stack at {id(self):x}, size={len(self)}>"

# Using the Stack class
s = Stack()
s.push('Dave')
s.push(42)

print(f"Stack length: {len(s)}")
print(f"Stack representation: {s}")

# The __repr__() method changes the way that a Stack is displayed and printed
# It's a good idea to always define __repr__() as it can simplify debugging 