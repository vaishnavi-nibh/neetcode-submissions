class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #take care of first edge case: are the strings different sizes
        #if strings are different sizes they cannot be anagrams
        if (len(s) != len(t)):
            return False
        
        #we want to initialize a dictionary that contains each letter and counts the frequency
        freq = {}

        for char in s:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1

        for char in t:
            if char in freq:
                freq[char] -= 1
            else:
                freq[char] = 1
        
        for value in freq.values():
            if value != 0:
                return False
        
        return True