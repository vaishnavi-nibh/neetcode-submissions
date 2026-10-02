class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #initialize maxProfit to be 0
        max_profit = 0

        #in this case we cannot have a buy and a sell
        if len(prices) < 2:
            return max_profit
        
        #set the minimum to the first element 
        min_price = prices[0]

        for i in range(1,len(prices)):
            #we will treat the current price we are on as the selling price, and see how much profit we make --> compare it against max profit and update maxprofit accordingly
            #if this price is lower than the minPrice thus far, we will update this to be the minPrice. the way we are doing this ensures that the minimum price in the left subarray we've explored thus far (before the current elem) is always maintained by minPrice.
            
            #and then the current price represents a candidate selling price and we want to see if this candidate selling price results in a profit higher than what we have achieved so far

            current_price = prices[i]
            curr_profit = current_price - min_price

            if curr_profit > max_profit:
                max_profit = curr_profit
            
            if current_price < min_price:
                min_price = current_price
        
        return max_profit