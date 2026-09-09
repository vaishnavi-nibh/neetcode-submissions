class Solution:
    def climbStairs(self, n: int) -> int:
        #dynamic programming solution 
        if n == 1:
            return 1

        dp = [0] * (n+1) #initializing an array of size n with 0s

        #"base case"
        dp[1] = 1
        dp[2] = 2

        #starting after n = 2
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2] #+1 method, or +2 method gives us num ways
        
        return dp[n]