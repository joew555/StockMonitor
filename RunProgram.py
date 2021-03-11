import StockInfo as si
import Music as ms

def run_program():

    while si.market_status() == "REGULAR":

        if si.current_price_minus_open() >= 0:

            ms.up()

        else:

            ms.down()
    else:

        print("The Market is Closed")

run_program()