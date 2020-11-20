from polygon import RESTClient


def main():
    key = "w8NGBOgXjp393pMbIBhHO6sOxN_N1x8E"

    # RESTClient can be used as a context manager to facilitate closing the underlying http session
    # https://requests.readthedocs.io/en/master/user/advanced/#session-objects
    with RESTClient(key) as client:
        resp = client.stocks_equities_daily_open_close("FB", "2020-11-17")
        print(f"On: {resp.from_} Apple opened at {resp.open} and closed at {resp.close}")



if __name__ == '__main__':
    main()

    # # Be sure to pip install websocket-client
    # # Details: https://pypi.org/project/websocket-client/
    #
    # import websocket
    #
    #
    # def on_message(ws, message):
    #     print(message)
    #
    #
    # def on_error(ws, error):
    #     print(error)
    #
    #
    # def on_close(ws):
    #     print("### closed ###")
    #
    #
    # def on_open(ws):
    #     ws.send('{"action":"auth","params":"YOUR_API_KEY"}')
    #     ws.send('{"action":"subscribe","params":"C.AUD/USD,C.USD/EUR,C.USD/JPY"}')
    #
    #
    # if __name__ == "__main__":
    #     # websocket.enableTrace(True)
    #     ws = websocket.WebSocketApp("wss://socket.polygon.io/forex",
    #                                 on_message=on_message,
    #                                 on_error=on_error,
    #                                 on_close=on_close)
    #     ws.on_open = on_open
    #     ws.run_forever()