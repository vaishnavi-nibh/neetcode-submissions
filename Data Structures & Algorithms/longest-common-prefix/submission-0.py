class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #start with the shortest string 
        prefix = min(strs, key=len)

        while prefix:

            count = 0

            for word in strs:
                if word.startswith(prefix):
                    count += 1
            
            if count == len(strs):
                return prefix
            
            prefix = prefix[:-1]
        
        #if we haven't returned yet, and prefix is empty 
        return ""