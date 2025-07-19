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
from readport import read_portfolio

if len(sys.argv) != 2:
    raise SystemExit(f"Usage: {sys.argv[0]} filename")

# File containing lines of the form ``name, share,  price``

filename = 'portfolio.csv'

portfolio = read_portfolio(filename)

total = sum([shares * price for _, shares, price in portfolio])
print(total)

total_shares = {s[0]: 0 for s in portfolio}
for name, shares, _ in portfolio:
    total_shares[name] += shares

print(total_shares)
