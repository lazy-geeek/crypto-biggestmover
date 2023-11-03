import pandas as pd

from exchange import exchange, ask_bid
from pprint import pprint

limit = 100


def df_sma(symbol, tf, sma):
    bars = exchange.fetch_ohlcv(symbol=symbol, timeframe=tf, limit=limit)
    # pprint(bars)
    df_sma = pd.DataFrame(
        bars, columns=["timestamp", "open", "high", "low", "close", "volume"]
    )
    df_sma["timestamp"] = pd.to_datetime(df_sma["timestamp"], unit="ms")

    sma_column = f"sma{sma}_{tf}"

    # SMA
    df_sma[sma_column] = df_sma.close.rolling(sma).mean()

    # if bid < sma then = BEARISH, if bid > sma = BULLISH
    bid = ask_bid(symbol)[1]

    # if sma > bid = SELL, if sma < bid = BUY
    df_sma.loc[df_sma[sma_column] > bid, "sig"] = "SELL"
    df_sma.loc[df_sma[sma_column] < bid, "sig"] = "BUY"

    df_sma["support"] = df_sma[:-1]["close"].min()
    df_sma["resis"] = df_sma[:-1]["close"].max()

    pprint(df_sma)


# RSI


def df_rsi(symbol, tf):
    bars = exchange.fetch_ohlcv(symbol=symbol, timeframe=tf, limit=limit)

    # pandas & TA, talib
    df_rsi = pd.DataFrame(
        bars, columns=["timestamp", "open", "high", "low", "close", "volume"]
    )
    df_rsi["timestamp"] = pd.to_datetime(df_rsi["timestamp"], unit="ms")
    # if bid < the 20 day sma then = BEARISH, if bid > 20 day sma = BULLISH
    bid = ask_bid(symbol)[1]

    # RSI
    rsi = RSIIndicator(df_rsi["close"])
    df_rsi["rsi"] = rsi.rsi()

    pprint(df_rsi)


# VWAP


def get_df_vwap(symbol, tf):
    bars = exchange.fetch_ohlcv(symbol, timeframe=tf, limit=limit)

    df_vwap = pd.DataFrame(
        bars, columns=["timestamp", "open", "high", "low", "close", "volume"]
    )

    df_vwap["timestamp"] = pd.to_datetime(df_vwap["timestamp"], unit="ms")

    lo = df_vwap["low"].min()
    hi = df_vwap["high"].max()
    l2h = hi - lo
    avg = (hi + lo) / 2

    return df_vwap


def vwap_indi(symbol, tf):
    # bring in the df and do this math super easy
    df_vwap = get_df_vwap(symbol, tf)

    # VWAP = (sum(first13valuesVolumexClose)) / (sum(volume colume top 13))

    # get volume x close
    df_vwap["volXclose"] = df_vwap["close"] * df_vwap["volume"]

    # get cummulative sum of vol here, which is the last vals together
    df_vwap["cum_vol"] = df_vwap["volume"].cumsum()

    # then cum sum of vol * price.. gonna do hi + low + close / 3 to get avg
    df_vwap["cum_volXclose"] = (
        df_vwap["volume"] * (df_vwap["high"] + df_vwap["low"] + df_vwap["close"]) / 3
    ).cumsum()

    # now i can get VWAP
    df_vwap["VWAP"] = df_vwap["cum_volXclose"] / df_vwap["cum_vol"]
    df_vwap = df_vwap.fillna(0)

    print(df_vwap)

    return df_vwap


def get_df_vwma(symbol):
    tf = "1d"
    # IF I CHNAGE THE ABOVE VARS.. MAKE SURE THAT THEY ARE == 24 hours
    # becuase VWAP is a 24 hour inidicator only.

    bars = exchange.fetch_ohlcv(symbol=symbol, timeframe=tf, limit=limit)
    df_vwma = pd.DataFrame(
        bars, columns=["timestamp", "open", "high", "low", "close", "volume"]
    )  # this is where is set the column titles in DF
    df_vwma["timestamp"] = pd.to_datetime(df_vwma["timestamp"], unit="ms")

    return df_vwma


def vwma_indi(symbol):
    df_vwma = get_df_vwma(symbol)

    df_vwma["SMA(41)"] = df_vwma.close.rolling(41).mean()
    df_vwma["SMA(20)"] = df_vwma.close.rolling(20).mean()
    df_vwma["SMA(75)"] = df_vwma.close.rolling(75).mean()

    df_sma = df_vwma.fillna(0)

    # now get VWMA

    vwmas = [20, 41, 75]
    for n in vwmas:
        df_vwma[f"sum_vol{n}"] = (
            df_vwma["volume"].rolling(min_periods=1, window=n).sum()
        )

        df_vwma["volXclose"] = (df_vwma["volume"]) * (df_vwma["close"])
        df_vwma[f"vXc{n}"] = df_vwma["volXclose"].rolling(min_periods=1, window=n).sum()

        # VWMA
        df_vwma[f"VWMA({n})"] = (df_vwma[f"vXc{n}"]) / (df_vwma[f"sum_vol{n}"])

        # this is for VWMA signals
        # df_vwma.loc[df_vwma[f'VWMA({n})'] > df_vwma['SMA(41)'], f'41sig{n}'] = 'BUY'
        # df_vwma.loc[df_vwma[f'VWMA({n})'] > df_vwma['SMA(20)'], f'20sig{n}'] = 'BUY'
        # df_vwma.loc[df_vwma[f'VWMA({n})'] > df_vwma['SMA(75)'], f'75sig{n}'] = 'BUY'

        # df_vwma.loc[df_vwma[f'VWMA({n})'] < df_vwma['SMA(41)'], f'41sig{n}'] = 'SELL'
        # df_vwma.loc[df_vwma[f'VWMA({n})'] < df_vwma['SMA(20)'], f'20sig{n}'] = 'SELL'
        # df_vwma.loc[df_vwma[f'VWMA({n})'] < df_vwma['SMA(75)'], f'75sig{n}'] = 'SELL'

    pprint(df_vwma)

    return df_vwma
