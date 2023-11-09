import talib
import pandas as pd

from backtesting import Strategy
from backtesting.lib import crossover


class RsiOscillator(Strategy):
    upper_bound = 70
    lower_bound = 30
    rsi_window = 14

    def init(self):
        price = self.data.Close
        self.rsi = self.I(talib.RSI, price, self.rsi_window)

    def next(self):
        if crossover(self.rsi, self.upper_bound):
            self.position.close()
        elif crossover(self.lower_bound, self.rsi):
            self.buy()


class SMAStrategy(Strategy):
    stop_loss_pct = 5
    take_profit_pct = 1
    entry_hour = 9
    exit_hour = 10

    def init(self):
        price = self.data.Close
        self.sma5 = self.I(talib.SMA, price, timeperiod=5)
        self.sma20 = self.I(talib.SMA, price, timeperiod=20)

    def next(self):
        price = self.data.Close[-1]
        hour = pd.Timestamp(self.data.index[-1]).to_pydatetime().hour

        if self.position:
            if hour >= self.entry_hour:
                self.position.close()

        else:
            if hour >= self.entry_hour and self.sma5[-1] < self.sma20[-1]:
                self.buy(
                    size=1000,
                    sl=price * (1 - (self.stop_loss_pct / 1000)),
                    tp=price * (1 + (self.take_profit_pct / 1000)),
                )


class RSIVWAPRSI(Strategy):
    # https://www.youtube.com/watch?v=FVSfN3_Xtqs&list=PLu5PUxcrztwWLK5SMyOsdtY9udo_5enBQ&index=4
    # TODO RSI-VWAP RSI Strategy aus Video Markus Adrian

    def init(self):
        pass

    def next(self):
        pass


class ICTSilverBullet(Strategy):
    # https://www.youtube.com/watch?v=d2wNBozYvAc&list=PLu5PUxcrztwWLK5SMyOsdtY9udo_5enBQ&index=5
    # TODO ICT Silver Bullet Strategy

    def init(self):
        pass

    def next(self):
        pass
