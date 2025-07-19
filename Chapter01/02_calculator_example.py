"""
Book: Python Distilled
Author: David M. Beazley
Publisher: Pearson
ISBN: 978-0-13-417327-6
"""

# Chapter 1.1 - Running Python
# Calculator Example - Interactive Python as Desktop Calculator

# Example calculations
result1 = 6000 + 4523.50 + 134.25
print(f"6000 + 4523.50 + 134.25 = {result1}")

# In interactive mode, the variable _ holds the result of the last operation
# This is useful if you want to use that result in subsequent statements
# Note: This variable only gets defined when working interactively

# Example of using the result in subsequent calculations
result2 = result1 + 8192.75
print(f"{result1} + 8192.75 = {result2}") 
