# pcost.py
#
# Exercise 1.27
import sys
import csv


def portfolio_cost(filename):
    cost = 0
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for line in rows:
            try:
                [_, share, price] = line
                cost = cost + int(share) * float(price)
            except ValueError:
                print("Couldn't parse", line)

    return cost


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print(f'Total coast: {cost:0.2f}')
