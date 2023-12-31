import zmq
import threading
import pandas as pd
import datetime
import time

from mt_socket import mt
from pprint import pprint

symbol = "EURUSD"
tf = "M5"
date_time = datetime.datetime(2023, 7, 1, 0, 0)
fromDate = time.mktime(date_time.timetuple())

# mt.construct_and_send(action="RESET")

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

pprint(df)
"""
mt.construct_and_send(action="RESET")
mt.construct_and_send(action="CONFIG", symbol="AUDUSD", chartTF="M1")
mt.construct_and_send(action="CONFIG", symbol="EURUSD", chartTF="M1")

def _t_livedata():
    socket = mt.live_socket()
    while True:
        try:
            last_candle = socket.recv_json()
        except zmq.ZMQError:
            raise zmq.NotDone("Live data ERROR")
        print(last_candle)


t = threading.Thread(target=_t_livedata, daemon=True)
t.start()

while True:
    pass
"""