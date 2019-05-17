import sys
import os
import threading
import requests
import time
import pprint

prices = { 'btc': 0.00 }

if len(sys.argv) < 2:
    print('please supply some coins to track')
    quit()

for coin in sys.argv[1:]:
    prices[coin] = 0.00

def update_price(coin):
    while True:
        template = 'https://api.bittrex.com/api/v1.1/public/getticker?market={}-{}'
        first_coin = 'usd' if coin == 'btc' else 'btc'
        pricing = requests.get(template.format(first_coin, coin)).json()
        prices[coin] = pricing['result']['Last']
        time.sleep(3)

for coin, price in prices.items():
    t = threading.Thread(target=update_price, args=(coin,))
    t.start()

while True:
    os.system('clear')
    for coin, price in prices.items():
        usd_price = price * prices['btc']
        if coin == 'btc':
            print('{} -> ${:.2f}'.format(coin.ljust(5), price))
        else:
            print('{} -> {:.8f} (${:.2f})'.format(coin.ljust(5), price, usd_price))
    time.sleep(.5)
