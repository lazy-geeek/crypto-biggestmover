from mt_socket import mt

"""
print(api.construct_and_send(action="CONFIG", symbol="AUDUSD", chartTF="M1"))
print(api.construct_and_send(action="CONFIG", symbol="EURUSD", chartTF="TICK"))

rep = api.construct_and_send(action="ACCOUNT")
print(rep)
"""


def _t_livedata():
    socket = api.live_socket()
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
