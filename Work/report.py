# report.py
#
# Exercise 2.4
import csv


def read_portfolio(filename):
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            record = dict(zip(headers, row))
            portfolio.append({'name': record['name'], 'shares': int(
                record['shares']), 'price': float(record['price'])})

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
