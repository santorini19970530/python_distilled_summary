"""
Book: Python Distilled
Author: David M. Beazley
Publisher: Pearson
ISBN: 978-0-13-417327-6
"""

# Chapter 1.16 - Objects and Classes
# Inheritance Example

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

# Inheritance example - MyStack with additional swap() method
class MyStack(Stack):
    def swap(self):
        if len(self._items) >= 2:
            self._items[-1], self._items[-2] = self._items[-2], self._items[-1]

# Using MyStack
s = MyStack()
s.push('Dave')
s.push(42)
print(f"Before swap: {s}")

s.swap()
print(f"After swap: {s}")

print(f"Popped item: {s.pop()}")
print(f"Popped item: {s.pop()}")

# Inheritance can also be used to change the behavior of an existing method
class NumericStack(Stack):
    def push(self, item):
        if not isinstance(item, (int, float)):
            raise TypeError("Expected an int or float")
        super().push(item)

# This would raise an error:
# s = NumericStack()
# s.push('Dave')  # TypeError: Expected an int or float 