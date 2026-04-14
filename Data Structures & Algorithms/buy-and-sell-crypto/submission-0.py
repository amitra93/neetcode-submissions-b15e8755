class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        buy = 0
        sell = 1
        maxProfit = 0
        while sell < len(prices):
            profit = prices[sell] - prices[buy]
            maxProfit = max(profit, maxProfit)
            if profit < 0:
                buy = sell
                sell = sell + 1
            else:
                sell = sell + 1
        return maxProfit
