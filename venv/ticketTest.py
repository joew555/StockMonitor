import Music as ms
import time as t
import datetime as dt
import stockPrompt as sp

from yahoo_fin import stock_info as si

#returns a dictionary - key value pair

stock = sp.stockName
stockQuote = si.get_quote_table(stock)

open = (round(stockQuote['Open'], 2))

def stockTrend():

    currentPrice = float(round(si.get_live_price(stock),2))

    print("Today's open price for " + stock + " was " + str(open))
    print("The current price for " + stock + " is " + str(currentPrice))
    if currentPrice >= open:
        ms.up()
    else:
        ms.down()

#while loop uses modulus to run every 5 minutes
while True:
    if dt.datetime.now().minute % 2 == 0:
        stockTrend()




