from http import client
import config
from binance.client import Client   
from binance.enums import *
import time
import datetime
import numpy as np

client = Client(config.API_KEY, config.API_SECRET, tld='com')
symbolTicker = 'BTCBUSD'
quantityOrders= 0.0013

def tendencia():
    x = []
    y = []
    sum = 0
    ma50_i = 0

    Resp = False
    
    klines = klines = client.get_historical_klines(symbolTicker, Client.KLINE_INTERNAL_15MINUTE, "18 hour ago UTC")
    if (len(klines) != 72):
        return False
    for i in range (56,72):  #16 VELAS DE 15 MIN C/U
        for j in range (i-50,i) #PARA CADA UNO DE ESOS 16 VOY A VER LA ULTIMA DE LAS 50 VELAS

def _ma59_():
    ma50_local = 0
    sum = 0
    klines = client.get_historical_klines(symbolTicker, Client.KLINE_INTERNAL_15MINUTE, "15 hour ago UTC")
    if(len(klines)==60):
        for i in range (10,60):
            sum = sum + klines[i][4]
        ma50_local = sum / 50
    return ma50_local

while 1: 
    orders= client.get_open_orders(symbol=symbolTicker)
    if (len(orders) !=0 ):
        print("HAY ORDENES ABIERTAS")
        time.sleep(10)
        continue

#GET PRICE / POR AHORA NO ENCONTRE UN GET CURRENT PRICE
    list_of_tickers = client.get_all_tickers()
    for tick_2 in list_of_tickers:
        if tick_2['symbol'] == symbolTicker:
            symbolPrice = tick_2['price']

ma50 = ma50_()
if (ma50 == 0): continue

print("" + symbolTicker + "*******")
print("Actual MA50" + symbolTicker + round(ma50,2))
print("Precio actual" + symbolTicker + round(symbolPrice,2))
print("Precio para comprar" + symbolTicker + round(symbolPrice*0.995,2))