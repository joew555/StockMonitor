import Music as ms
import time as t
import datetime as dt
import stockPrompt as sp

from yahoo_fin import stock_info as si

# returns a dictionary - key value pair

stock = sp.stockName
stock_table = si.get_quote_data(stock)


def open_price():

    open = (round(stock_table['regularMarketOpen'], 2))

    return open



def current_price():

    current = (round(stock_table['regularMarketPrice'], 2))

    return current


def current_price_minus_open():

    current = current_price() - open_price()
    round(current, 2)

    return current

def market_status():
    
    status = si.get_market_status()
    
    return status

print(stock_table)
print(open_price())
print(current_price())
print(current_price_minus_open())
print(si.get_market_status())








# #while loop uses modulus to run every 5 minutes
# while True:
#     if dt.datetime.now().minute % 2 == 0:
#         stockTrend()


# def stockTrend():
#
#     currentPrice = float(round(si.get_live_price(stock),2))
#
#     print("Today's open price for " + stock + " was " + str(open))
#     print("The current price for " + stock + " is " + str(currentPrice))
#     if currentPrice >= open:
#         ms.up()
#     else:
#         ms.down()
#
# #while loop uses modulus to run every 5 minutes
# while True:
#     if dt.datetime.now().minute % 2 == 0:
#         stockTrend()
