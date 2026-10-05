class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #the valid window cannot contain any duplicates
        #the window is defined by two pointers (left pointer and right pointer)

        #when the right pointer (which is what is going through the current elements) wants to add something to the substring, it needs to make sure the no duplicate-invariant is preserved. in the case it is violated, the right pointer needs to increment until the invariant is reinstated.

        max_length = 0
        
        if len(s) == 0:
            return max_length
        
        left = 0 #this marks the left of the subwindow
        for i in range(len(s)):
            current_elem = s[i]
            while current_elem in s[left:i]:
                left += 1
            
            substr_len = i - left + 1

            if substr_len > max_length:
                max_length = substr_len
        
        return max_length
            

        