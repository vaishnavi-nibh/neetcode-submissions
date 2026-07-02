class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0;
        j = len(s) - 1
        
        s = s.lower()
        #while the pointers dont cross
        while (i < j):
            if not s[i].isalnum():
                i += 1
                continue
            if not s[j].isalnum():
                j -= 1
                continue
            
            #now that we skipped non-alphanumeric characters, we actually compare
            if s[i] != s[j]:
                return False;
            
            i += 1
            j -= 1

        #recall function has to actually return something lol
        return True