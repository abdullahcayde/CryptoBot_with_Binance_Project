import  json, pprint, numpy as np
import  pandas as pd
import websocket, talib

import config
from binance.client import Client
from binance.enums import *

# unixtimestamp.com
# https://ta-lib.github.io/ta-lib-python/func_groups/momentum_indicators.html ==> RSI - Relative Strength Index 
# NOTE: The RSI function has an unstable period. real = RSI(close, timeperiod=14)
# python-binance

# Create Client
client = Client(config.APIKey, config.SecretKey)

SOCKET = "wss://stream.binance.com:9443/ws/ethusdt@kline_1m"

RSI_PERIOD = 14
RSI_OVERBOUGHT = 70
RSI_OVERSOLD = 30
TRADE_SYMBOL = 'ETHUSD'
TRADE_QUANTITY = 0.053 # 100$

closes =[]
in_position = False
df01 = pd.DataFrame()
my_list = []

def order(side, quantity, symbol,order_type=ORDER_TYPE_MARKET):
    try:
        print("sending order")
        #order = client.create_order(symbol=symbol, side=side, type=order_type, quantity=quantity)
        order = "ok"
        print(order)
    except Exception as e:
        print(f"an exception occured - {e}")
        return False

    return True


def on_open(ws):
    print('opened connection')

def on_close(ws):
    print('closed connection')

def on_message(ws, message):
    global closes, in_position
    
    print('recieved message')
    json_message = json.loads(message)
    pprint.pprint(json_message)

    my_list.append(json_message)

    """


    candle = json_message['k']

    is_candle_closed = candle['x']
    close = candle['c']

    if is_candle_closed:
        print(f'candle closed at {close}')
        closes.append(float(close))
        print("closes")
        print(closes)

        if len(closes) > RSI_PERIOD:
            np_closes = np.array(closes)
            rsi = talib.RSI(np_closes, RSI_PERIOD)
            print('all rsi calculated')
            print(rsi)
            last_rsi = rsi[-1]
            print(f'the current rsi is {last_rsi}')

            if last_rsi > RSI_OVERBOUGHT:
                if in_position:
                    print("Overbought! Sell! Sell! Sell!")
                    # put binance sell logic here
                    ##order_succeeded = order(SIDE_SELL, TRADE_QUANTITY, TRADE_SYMBOL)
                    #if order_succeeded:
                        #in_position = False
                else:
                    print("It is overbought, but we don't own any. Nothing to do.")
            
            if last_rsi < RSI_OVERSOLD:
                if in_position:
                    print("It is oversold, but you already own it, nothing to do.")
                else:
                    print("Oversold! Buy! Buy! Buy!")
                    # put binance buy order logic here
                    ##order_succeeded = order(SIDE_BUY, TRADE_QUANTITY, TRADE_SYMBOL)
                    #if order_succeeded:
                        #in_position = True
"""
ws = websocket.WebSocketApp(SOCKET, on_open=on_open , on_close=on_close, on_message=on_message)
ws.run_forever()



