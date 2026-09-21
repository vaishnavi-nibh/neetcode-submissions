class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        #defining a combined new string
        output_str = ""
        i = 0 

        while i < len(word1) and i < len(word2):
            output_str += word1[i]
            output_str += word2[i]
            i += 1
        
        if len(word1) > len(word2):
            output_str += word1[i:]
        
        if len(word2) > len(word1):
            output_str += word2[i:]
        
        return output_str
