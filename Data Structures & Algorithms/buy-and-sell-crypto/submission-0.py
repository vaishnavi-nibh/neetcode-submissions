class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        #initial
        max_profit = 0

        for i in range(len(prices) - 1):
            buy = prices[i]
            sell = max(prices[i+1:]) #everything to the right is potential sell things
            if buy > sell:
                continue
            elif buy <= sell:
                profit = sell - buy
            
            if profit > max_profit:
                max_profit = profit
        
        return max_profit
                