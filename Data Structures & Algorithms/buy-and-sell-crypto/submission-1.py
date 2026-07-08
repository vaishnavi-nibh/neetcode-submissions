class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = prices[0]

        for i in range(1, len(prices)):
            current = prices[i]
            if current < min_price:
                min_price = current
                continue

            profit = current - min_price
            if profit > max_profit:
                max_profit = profit
        
        return max_profit
