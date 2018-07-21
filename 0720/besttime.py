class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """

    def maxProfit1(self, prices):
        from sys import  maxint
        profit = 0
        low = maxint
        for price in prices:
            profit = max(profit, price-profit)
            low = min(low, price)
        return profit

    def maxProfit2(self, prices):
        profit = 0
        for i in range(len(prices)-1):
            profit += max(prices[i+1]-prices[i], 0)
        return profit

    def maxProfit3(self, prices):