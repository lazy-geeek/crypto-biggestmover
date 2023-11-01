import MetaTrader5 as mt

from decouple import config

login = config("MT_ACCOUNT")
password = config("MT_PASSWORD")
server = config("MT_SERVER")

mt.initialize()
mt.login(login, password, server)
