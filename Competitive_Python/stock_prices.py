'''
Stock Prices Calculation...
Author: Pavan Kumar Paluri
'''

'''
Description:
Given list of stock prices, the buyer has to buy stock at mimimum prices,
wait for atleast 1 minute and can then sell at its highest price...
'''

stock_prices = [7, 4, 1, 6, 5]


def max_profit(prices) -> int:
    '''
    let low price be inf initially
    :param prices:
    :return:
    '''
    profit = 0
    price_low = float('inf')
    for price in prices:
        if price < price_low:
            price_low = price
        else:
            profit = max(profit, price-price_low)
    return profit


if __name__ == '__main__':
    print(max_profit(stock_prices))