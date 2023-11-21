import numpy as np
import pandas as pd
import multiprocessing as mp

from backtesting import Backtest
from mt_broker import mt
from datetime import datetime
from pprint import pprint

from backtesting_strategies import SMAStrategy, RsiOscillator

mp.set_start_method("fork")

symbol = "EURUSD"
tf = mt.TIMEFRAME_M5
date_from = datetime(2022, 1, 1)
date_to = datetime.now()

rates = mt.copy_rates_range(symbol, tf, date_from, date_to)
mt_df = pd.DataFrame(rates)

mt_df["time"] = pd.to_datetime(mt_df["time"], unit="s")

data = mt_df.rename(
    columns={
        "open": "Open",
        "high": "High",
        "low": "Low",
        "close": "Close",
        "tick_volume": "Volume",
    }
)
data = data.drop(["spread", "real_volume"], axis=1)
data = data.set_index("time")

bt = Backtest(data, RsiOscillator, cash=100000, commission=0.00007)

stats = bt.optimize(
    upper_bound=range(50, 85, 5),
    lower_bound=range(15, 45, 5),
    rsi_window=range(10, 30, 2),
    maximize="Equity Final [$]",
)


"""
output = bt.optimize(
    maximize="Equity Final [$]",
    stop_loss_pct=range(5, 20),
    take_profit_pct=range(1, 10),
)
print(output)

"""

# stats = bt.run()
print(stats)
# bt.plot(resample=False)
