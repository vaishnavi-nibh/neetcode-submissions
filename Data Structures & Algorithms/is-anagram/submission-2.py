class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #handle case where the strings are of different lengths
        if len(s) != len(t):
            return False
        
        #if the strings are of the same length
        #make a frequency map, with each letter and its frequency
        freq = {}

        for char in s:
            if char not in freq:
                freq[char] = 1
            else:
                freq[char] += 1

        #now lets go through the other string and compare frequencies by decrementing 
        for char in t:
            #if the char is not in freq now, it cannot be a valid anagram (because that means t has a char that s doesnt)
            if char not in freq:
                return False
            else:
                freq[char] -= 1

        #now, we go through freq to check if it has any nonzero values,
        #if freq has nonzero values that means that it is not an anagram because the two strings dont have the same exact characters with the same exact frequency. 
        for val in freq.values():
            if val != 0:
                return False
        
        return True
            