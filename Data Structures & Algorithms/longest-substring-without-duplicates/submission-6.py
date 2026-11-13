class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #longest substring without repeating characters is defined by a valid window
        #edge case, empty string --> return 0
        max_length = 0
        if len(s) == 0:
            return max_length
        
        #start a left pointer, this maintains the left of our valid substring
        #then the right pointer is maintained as we are iterating through the string (searching pointer)
        left = 0
        for i in range(len(s)):
            #incrementing the left window, to maintain valid window invariant
            while s[i] in s[left:i]:
                left += 1
            
            #adding the current elem to the valid window
            curr_length = i - left + 1

            if curr_length > max_length:
                max_length = curr_length
            
        return max_length