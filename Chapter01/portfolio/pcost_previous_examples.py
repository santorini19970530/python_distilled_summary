"""
Book: Python Distilled
Author: David M. Beazley
Publisher: Pearson
ISBN: 978-0-13-417327-6
"""

# pcost.py
#
# Reads input lines of the form 'NAME, SHARES, PRICE'.
#
# For example:
#
#   SYM,123,456.78

import sys

if len(sys.argv) != 2:
    raise SystemExit(f"Usage: {sys.argv[0]} filename")

rows = []
with open(sys.argv[1], 'rt') as file:
    for line in file:
        rows.append(line.split(','))

# rows is a list of this form
# [
#   ['SYM', '123', '456.78']
# ...
# ]

total = sum([ int(row[1]) * float(row[2]) for row in rows ])
print(f'Total cost: {total:0.2f}')

# File containing lines of the form ``name, share,  price``

portfolio = []

with open('portfolio.csv') as file:
    for line in file:
        row = line.split(',')
        name = row[0]
        shares = int(row[1])
        price = float(row[2])
        holding = (name, shares, price)
        portfolio.append(holding)

total = sum([shares * price for _, shares, price in portfolio])
print(total)

# dictionaries

portfolio = [
    ('ACME', 50, 92.34),
    ('IBM', 75, 102.25),
    ('PHP', 40, 74.50),
    ('IBM', 50, 124.75)
]

total_shares = {s[0]: 0 for s in portfolio}
for name, shares, _ in portfolio:
    total_shares[name] += shares

print(total_shares)
