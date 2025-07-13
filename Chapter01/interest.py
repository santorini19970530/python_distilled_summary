#interest.py

princinpal = 1000   # initial amount
rate = 0.05         # interest rate
numyears = 5        # number of years
year = 1

while year <= numyears:
    princinpal *= (1 + rate)
    print(f"{year:>3d} {princinpal:0.2f}")
    year += 1
