import ccxt
import math
import pandas as pd
import time, schedule
import warnings
import numpy as np

from decouple import config
from pprint import pprint
from datetime import datetime

###################### INPUTS ###################

symbol = 'ETHUSD'
size = 50000
lockout_loss = 5000
mo_size = size / 4
leverage = 30
num_orders = 2
max_time = 4200
max_daily_trades = 3

traget = 800
max_loss = -37

tp_spread = 2
target_multiple = 3

#################################################

phemex_config = {
    'enableRateLimit': True,
    'apiKey': config("PHEMEX_TESTNET_ID"),
    'secret': config("PHEMEX_TESTNET_SECRET"),
    #'test': True    
    }

phemex = ccxt.phemex(phemex_config)
phemex.set_sandbox_mode(True)

bal = phemex.fetch_balance()
pprint(bal)

def max_daily_trades():
    
    max = max_daily_trades
    closed = phemex.fetch_closed_orders(symbol)
    closed_df = pd.DataFrame.from_dict(closed)
    closed_df = closed_df[['filled', 'lastTradeTimestamp']]
    pprint(closed_df)
    

# max_daily_trades()