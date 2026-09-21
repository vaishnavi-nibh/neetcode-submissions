class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        #defining a combined new string
        output_str = ""

        #defining a pointer for string1 and a pointer for string2
        i = 0 #word1
        j = 0 #word2

        while i < len(word1) and j < len(word2):
            output_str += word1[i]
            output_str += word2[j]
            i += 1
            j += 1
        
        if len(word1) > len(word2):
            output_str += word1[i:]
        
        if len(word2) > len(word1):
            output_str += word2[j:]
        
        return output_str
