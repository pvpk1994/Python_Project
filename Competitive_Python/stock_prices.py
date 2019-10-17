'''
Stock Prices Calculation...
Author: Pavan Kumar Paluri
'''

'''
Description:
Given list of stock prices, the buyer has to buy stock at mimimum prices,
wait for atleast 1 minute and can then sell at its highest price...
'''

stock_prices = [9, 7, 9, 9, 9]


def get_max_profit(list_stocks: list) -> int:
    if len(list_stocks) == 1:
        raise AssertionError("Only one stock")
    # if sell happens before buy, invalidate that case..
    # To acheive that, get the indices of both max and min
    if list_stocks.index(min(list_stocks)) <= list_stocks.index(max(list_stocks)):
        buy = min(list_stocks)
        sell = max(list_stocks)
        profit = sell - buy
        if profit > 0:
            print(f'The profit made is:{profit}')
            return profit
        elif profit == 0:
            print(f'The profit is: {profit}')
            return profit
        else:
            print(f'Profit is: {profit}')
    # Implies, the price is constantly going down...
    # In such a case return min negative profit.
    else:
        profit = list_stocks[1] - list_stocks[0]
        return profit


get_max_profit(stock_prices)