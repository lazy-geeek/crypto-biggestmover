Sure, I can help you with that. Here is the backtest code for the provided trading strategy using the backtesting.py module. 

```python
from backtesting import Backtest, Strategy
from backtesting.lib import SignalStrategy
from backtesting.test import EURUSD, SMA

class BreakoutEngulfingStrategy(Strategy):
    def init(self):
        # Set the trend by using a moving average crossover
        self.trend = self.I(SMA, self.data.Close, 50) > self.I(SMA, self.data.Close, 200)
        
    def next(self):
        if self.data.High > max(self.data.High[:-1]) and self.trend:
            # Bullish breakout
            if self.data.Low == min(self.data.Low[-2], self.data.Low[-1]):
                self.buy()
        elif self.data.Low < min(self.data.Low[:-1]) and not self.trend:
            # Bearish breakout
            if self.data.High == max(self.data.High[-2], self.data.High[-1]):
                self.sell()
                
class BreakoutEngulfing(Strategy):
    def init(self):
        # Set the trend by using a moving average crossover
        self.trend = self.I(SMA, self.data.Close, 50) > self.I(SMA, self.data.Close, 200)
        
    def next(self):
        if self.trend:
            # Bullish engulfing entry
            if self.data.Open[-1] > self.data.Close[-1] and self.data.Close > self.data.Open and self.data.Close[-1] < self.data.Open[-1] and self.data.Close[-1] > self.data.Open:
                self.buy()
        else:
            # Bearish engulfing entry
            if self.data.Open[-1] < self.data.Close[-1] and self.data.Close < self.data.Open and self.data.Close[-1] > self.data.Open[-1] and self.data.Close[-1] < self.data.Open:
                self.sell()
                
bt = Backtest(EURUSD, BreakoutEngulfing,
              cash=10000, commission=0.002,
              exclusive_orders=True)
stats = bt.run()
stats
```