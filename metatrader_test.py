import pandas as pd

from datetime import datetime
from pprint import pprint

from mt_broker import mt

ticker = "EURUSD"
tf = mt.TIMEFRAME_M5
starting_point = datetime.now()
no_of_candles = 10000

rates = mt.copy_rates_from(ticker, tf, starting_point, no_of_candles)
ohlc = pd.DataFrame(rates)
ohlc["time"] = pd.to_datetime(ohlc["time"], unit="s")

pprint(ohlc)

account_info = mt.account_info()
no_of_symbols = mt.symbols_total()
symbols = mt.symbols_get()
symbol = mt.symbol_info("EURUSD")._asdict()
