class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0 
        #edge case where the prices array has less than two elements
        if len(prices) < 2:
            return max_profit 
        
        minimum = prices[0]
        #treat the first price as the minimum

        for i in range(1, len(prices)):
            #treat the current price as potential sell price, and the minimum is the buy price
            profit = prices[i] - minimum

            if profit > max_profit:
                max_profit = profit

            if prices[i] < minimum:
                minimum = prices[i]    

        return max_profit    
