import pandas as pd
import onecall
import time
import schedule

from decouple import config
from pprint import pprint

size = 1
symbol = 'BTCUSD'

onecall = onecall.phemex(
    key=config("PHEMEX_ID"),
    secret=config("PHEMEX_SECRET"),
    debug=True
)

def ask_bid(symbol=symbol):
    # orderbook data

    ob = onecall.get_orderbook(symbol,False)
    ask = ob['result']['book']['asks'][0][0]
    bid = ob['result']['book']['bids'][0][0]    
    
    return ask, bid

def bot():
    askbid = ask_bid(symbol)
    ask = askbid[0]
    bid = askbid[1]

    #onecall.limit_order(symbol, onecall.BUY_SIDE, size, bid)
    #onecall.limit_order(symbol, onecall.SELL_SIDE, size, ask)

    print(ask)
    print(bid)

# identify biggest movers % up and down

bot()


