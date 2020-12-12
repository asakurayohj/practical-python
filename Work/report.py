# report.py
#
# Exercise 2.4
import csv


def read_portfolio(filename):
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        next(rows)
        for row in rows:
            portfolio.append(
                {'name': row[0], 'shares': int(row[1]), 'price': float(row[2])})

    return portfolio


def read_prices(filename):
    prices = {}
    with open(filename) as f:
        rows = csv.reader(f)
        for row in rows:
            if not row:
                pass
            else:
                name, price = row
                prices[name] = float(price)

    return prices


def make_report(portfolio, prices):
    report = []
    for stock in portfolio:
        name = stock['name']
        shares = stock['shares']
        price = stock['price']
        change = prices[name] - price
        report.append((name, shares, '$'+str(price), change))
    headers = ('Name', 'Shares', 'Price', 'Change')
    print(
        f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
    sep = '----------'
    print(f'{sep:>10s} {sep:>10s} {sep:>10s} {sep:>10s}')
    for r in report:
        print('%10s %10d %10s %10.2f' % r)

# total_cost = 0.0
# portfolio = read_portfolio('Data/portfolio.csv')
# for item in portfolio:
#     total_cost = total_cost + item['shares']*item['price']

# cur_total = 0.0

# prices = read_prices('Data/prices.csv')
# for item in portfolio:
#     name = item['name']
#     shares = item['shares']
#     price = prices.get(name, item['price'])
#     gain = shares * (price - item['price'])
#     print(
#         f'{name:>6s}{shares:>6d}{item["price"]:>10.2f}{price:>10.2f}{gain:>10.2f}')
#     cur_total = cur_total + shares * price


# print(total_cost, cur_total)
