class Solution:
    def maxProfit_1(self, prices: List[int]) -> int:
        cur_hold, cur_not_hold = -float('inf'), 0
        for stock_price in prices:
            cur_hold, cur_not_hold = max(cur_hold, cur_not_hold - stock_price), max(cur_not_hold, cur_hold + stock_price)
        return cur_not_hold

    def maxProfit_2(self, prices: List[int]) -> int:
        " same idea as method 3; but with a dp list (?) "
        price_gain = []  # store all positive (prices[i+1]-prices[i]) values
        for i in range(len(prices)-1):
            if prices[i] < prices[i+1]:
                price_gain.append(prices[i+1]- prices[i])
        return sum(price_gain)

    def maxProfit_3(self, prices: List[int]) -> int:
        " from day X, the buying day will be the last continuous day that the price is smallest. "
        prices.append(0)
        profit = 0
        buy_price = prices[0]
        for i in range(len(prices)):
            if prices[i] < prices[i - 1]:
                profit += prices[i - 1] - buy_price
                buy_price = prices[i]
        return profit