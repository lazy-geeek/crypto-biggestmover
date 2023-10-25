from indicators import df_sma, df_rsi, vwap_indi, vwma_indi

tf = "15m"
limit = 100
sma = 20

symbol = "BTCUSDT"

# df_sma(symbol=symbol, tf=tf, sma=sma)
# df_rsi(symbol, tf)
# vwap_indi(symbol, tf)
vwma_indi(symbol)
