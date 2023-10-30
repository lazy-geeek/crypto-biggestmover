import MetaTrader5 as mt

from decouple import config
from datetime import datetime
from pprint import pprint

login = config("MT_ACCOUNT")
password = config("MT_PASSWORD")
server = config("MT_SERVER")

ticker = "EURUSD"
tf = mt.TIMEFRAME_M5
starting_point = datetime.now()
no_of_candles = 10000

mt.initialize()
mt.login(login, password, server)

rates = mt.copy_rates_from(ticker, tf, starting_point, no_of_candles)

account_info = mt.account_info()
no_of_symbols = mt.symbols_total()
symbols = mt.symbols_get()
symbol = mt.symbol_info("EURUSD")._asdict()

pprint(symbol["name"])
