class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #we want to see what the maximum profit we can achieve is: so we want to find the lowest buy price and the highest sell price
        #initializing maxProfit = 0
        maxProfit = 0

        #in the case that the length of the array is less than 2 (0 or 1) there is no profit generated, cuz there won't be a buying and selling pair
        if len(prices) < 2:
            return maxProfit
        
        minPrice = prices[0] #set the first element to be the minimum price

        for i in range(1, len(prices)):
            sellPrice = prices[i]
            currProfit = sellPrice - minPrice

            if currProfit > maxProfit:
                maxProfit = currProfit

            if sellPrice < minPrice:
                minPrice = sellPrice
            
        return maxProfit
            

            