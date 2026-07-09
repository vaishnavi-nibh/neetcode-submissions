class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #define a set seen, to keep track of if we've seen a character or not
        seen = set()
        max_length = 0
        
        #pointer to keep track of start of valid window
        left = 0

        for i in range(len(s)):
            while s[i] in seen:
                seen.remove(s[left])
                left += 1

            #valid substring case (no duplicates in the substring)
            #add the current element to the set of elements we've explored (because they are all unique)
            seen.add(s[i])
            #track the current substring length by using the right (i) and left pointers 
            s_length = i - left + 1
            #compare against max_length 
            if s_length > max_length:
                max_length = s_length
        
        
        return max_length
            


