import zmq
import threading
import pandas as pd
import datetime
import time
import multiprocessing as mp

from backtesting import Backtest
from backtesting_strategies import SMAStrategy, RsiOscillator
from mt_socket import mt
from pprint import pprint

symbol = "EURUSD"
tf = "M5"
date_time = datetime.datetime(2023, 7, 1, 0, 0)
fromDate = time.mktime(date_time.timetuple())

response = mt.construct_and_send(action="HISTORY", actionType="DATA", symbol=symbol, chartTF=tf, fromDate=fromDate)
df = pd.DataFrame(response['data'])

df.drop(df.columns[6], axis=1, inplace=True)
df[0] = pd.to_datetime(df[0], unit="s")
df.set_index(0, inplace=True)
columns={
        df.columns[0]: "Open",
        df.columns[1]: "High",
        df.columns[2]: "Low",
        df.columns[3]: "Close",
        df.columns[4]: "Volume"
}
df.rename(columns=columns, inplace=True)

# pprint(df)

bt = Backtest(df, RsiOscillator, cash=100000, commission=0.00007)


stats = bt.optimize(
    upper_bound=range(50, 85, 1),
    lower_bound=range(15, 45, 1),
    rsi_window=range(2, 50, 1),
    maximize="Equity Final [$]",
)

# stats = bt.run()

print(stats)
pprint(stats["_strategy"])
