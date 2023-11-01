import backtrader as bt
import pandas as pd

from datetime import datetime
from mt_broker import mt

ticker = "EURUSD"
tf = mt.TIMEFRAME_M5
starting_point = datetime.now()
no_of_candles = 10000

rates = mt.copy_rates_from(ticker, tf, starting_point, no_of_candles)
mt_df = pd.DataFrame(rates)
mt_df["time"] = pd.to_datetime(mt_df["time"], unit="s")

data = bt.feeds.PandasData(
    dataname=mt_df,
    datetime=0,
    open=1,
    high=2,
    low=3,
    close=4,
    volume=5,
    openinterest=-1,
)

cerebro = bt.Cerebro(stdstats=False)
cerebro.addstrategy(bt.Strategy)
cerebro.adddata(data)
cerebro.run()
cerebro.plot(style="bar")
