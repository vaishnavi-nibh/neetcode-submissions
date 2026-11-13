class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #edge case: if the length of the prices array is less than 2, then we cant engage in a buying-selling transaction (only 1 element), so profit is 0
        maxProfit = 0

        if len(prices) < 2:
            return maxProfit

        minPrice = prices[0]

        for i in range(1, len(prices)):
            #we treat each new price we are iterating on as a candidate selling price
            currPrice = prices[i]
            currProfit = currPrice - minPrice

            if currProfit > maxProfit:
                maxProfit = currProfit
            
            #if the current price we are examining is smaller than the minimum, then we update the minimum and treat the current price as our "buy price".
            if currPrice < minPrice:
                minPrice = currPrice 
        
        return maxProfit
            