class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #they have the same characters, and with the same frequency
        #s = apple, t = aapple --> not a valid anagram
        
        #if the lengths of the strings are different, not a valid anagram
        if len(s) != len(t):
            return False

        #using a dictionary that maintains frequencies
        freq = {}

        for char in s:
            if char not in freq:
                freq[char] = 1
            else:
                freq[char] += 1
        

        for char in t:
            if char not in freq:
                return False
            else:
                freq[char] -= 1
        
        for val in freq.values():
            if val != 0:
                return False
        
        return True

            
