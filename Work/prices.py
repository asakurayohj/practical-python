import csv


def read_prices(filename):
    prices = {}
    with open(filename) as f:
        rows = csv.reader(f)
        for row in rows:
            if not row:
                pass
            else:
                name, price = row
                prices[name] = price

    return prices
