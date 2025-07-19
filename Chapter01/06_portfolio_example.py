"""
Book: Python Distilled
Author: David M. Beazley
Publisher: Pearson
ISBN: 978-0-13-417327-6
"""

# Chapter 1.8 - Lists
# Portfolio Example

# Portfolio data as a list of tuples
portfolio = [
    ('AA', 100, 32.2),
    ('IBM', 50, 91.1),
    ('CAT', 150, 83.44),
    ('MSFT', 200, 51.23),
    ('GE', 95, 40.37),
    ('MSFT', 50, 65.1),
    ('IBM', 100, 70.44)
]

# Accessing individual records
print("First record:")
print(portfolio[0])

print("\nSecond record:")
print(portfolio[1])

# Accessing individual fields
print(f"\nNumber of IBM shares: {portfolio[1][1]}")
print(f"IBM share price: {portfolio[1][2]}")

# Looping over all records and unpacking fields
print("\nPortfolio summary:")
for name, shares, price in portfolio:
    print(f"{name:>10} {shares:>10} {price:>10.2f}")

# Calculate total value
total_value = sum(shares * price for name, shares, price in portfolio)
print(f"\nTotal portfolio value: ${total_value:,.2f}") 
