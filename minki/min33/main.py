class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy_in = -1
        for i in range(len(prices)-1):
            if prices[i] > prices[i+1] and buy_in != -1:
                profit +=  prices[i] - prices[buy_in]
                buy_in = -1
                
            if prices[i] <= prices[i+1] and buy_in == -1:
                buy_in = i
        if buy_in != -1:
            profit += prices[-1] - prices[buy_in]
        return profit
