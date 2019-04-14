# READ

# into pandas DataFrame
import pandas as pd

btc = pd.read_csv('btc_daily.csv')
print(btc.dtypes)
print(btc['Price'])
btc['Price'] = btc['Price'].apply(lambda p: p.replace(',', ''))
btc['Price'] = btc['Price'].apply(Decimal) # avoid float imprecision
btc['Price'] = btc['Price'].apply(lambda p: round(p,2))
print(btc['Price'])

# process using standard csv

import csv
with open('stocks.csv') as f:
    f_csv = csv.DictReader(f)
    for row in f_csv:
        # process row
        # access using row header (row['Symbol'])


# WRITE
headers = ['Symbol', 'Price']
rows = [('AA', 13.87), ('AIG', 35.65)]
with open('stocks.csv') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(headers)
    f_csv.writerows(rows)

# if data is series of dicts
headers = ['Symbol', 'Price']
rows = [{'Symbol':'AA', 'Price':13.87}, {'Symbol':'AIG', 'Price':35.65}]
with open('stocks.csv', 'w') as f:
    f_csv = csv.DictWriter(f, headers)
    f_csv.writeheader()
    f_csv.writerows(rows)
