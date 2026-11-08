class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        left = 0
        max_substr = 0

        #sliding window, the window holds a valid substring which doesn't have repeating characters
        for i in range(len(s)):
            curr = s[i]

            while curr in s[left:i]:
                left += 1
            
            #if the while loop has ended, curr is no longer in s[left:i] so we can add it
            curr_substr = i - left + 1

            if curr_substr > max_substr:
                max_substr = curr_substr
        
        return max_substr