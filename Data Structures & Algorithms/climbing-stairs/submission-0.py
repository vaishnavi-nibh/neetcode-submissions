class Solution:
    def climbStairs(self, n: int) -> int:
        #memoization approach
        memo = {} #defining the dictionary that will hold the ways to get to step n

        def climb(n) -> int:
            #defining the base cases
            #if n = 1, there is only 1 way to get there
            if n == 1:
                return 1
            
            #if n = 2, there are 2 ways to get there: 1 + 1 or 2
            if n == 2:
                return 2
            
            #if we already calculated the number of ways to get to a specific n, no need to recompute
            if n in memo:
                return memo[n]

            #otherwise if it doesn't exist, lets compute the num ways to get to n and then make sure we store it

            memo[n] = climb(n-1) + climb(n-2)

            return memo[n]
        
        return climb(n)
