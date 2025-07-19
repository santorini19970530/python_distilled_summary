"""
Book: Python Distilled
Author: David M. Beazley
Publisher: Pearson
ISBN: 978-0-13-417327-6
"""

# Chapter 1.16 - Objects and Classes
# Calculator Example - Composition over Inheritance

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

# Calculator using composition (has-a relationship) rather than inheritance
class Calculator:
    def __init__(self):
        self._stack = Stack()
    
    def push(self, value):
        self._stack.push(value)
    
    def pop(self):
        return self._stack.pop()
    
    def add(self):
        b = self._stack.pop()
        a = self._stack.pop()
        self._stack.push(a + b)
    
    def sub(self):
        b = self._stack.pop()
        a = self._stack.pop()
        self._stack.push(a - b)
    
    def mul(self):
        b = self._stack.pop()
        a = self._stack.pop()
        self._stack.push(a * b)
    
    def div(self):
        b = self._stack.pop()
        a = self._stack.pop()
        self._stack.push(a / b)

# Using the Calculator
# Calculate 2 + 3 * 4
calc = Calculator()
calc.push(2)
calc.push(3)
calc.push(4)
calc.mul()  # 3 * 4 = 12
calc.add()  # 2 + 12 = 14
result = calc.pop()
print(f"2 + 3 * 4 = {result}")

# This approach uses composition (Calculator has a Stack)
# rather than inheritance (Calculator is a Stack)
# This is often a better design choice 