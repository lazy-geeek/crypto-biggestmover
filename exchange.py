import ccxt

from decouple import config

exchange_config = {
    'enableRateLimit': True,
    #'apiKey': config("PHEMEX_TESTNET_ID"),
    #'secret': config("PHEMEX_TESTNET_SECRET")    
    'apiKey': config("PHEMEX_ID"),
    'secret': config("PHEMEX_SECRET")    
    }

exchange = ccxt.phemex(exchange_config)
#exchange.set_sandbox_mode(True)

def ask_bid(symbol):

    ob = exchange.fetch_order_book(symbol)    

    bid = ob['bids'][0][0]
    ask = ob['asks'][0][0]

    return ask, bid # ask_bid()[0] = ask , [1] = bid