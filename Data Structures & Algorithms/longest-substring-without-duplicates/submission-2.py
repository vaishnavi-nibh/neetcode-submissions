class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        max_substr = 1
        left = 0 #to begin with
        curr = 0 #initially setting the current element we're looking at to 0


        while curr < len(s):
            while s[curr] in s[left:curr]:
                left += 1 #making the left window not contain it
            
            curr_length = curr - left + 1

            if curr_length > max_substr:
                max_substr = curr_length
            
            curr += 1
        
        return max_substr