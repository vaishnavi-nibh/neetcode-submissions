class Solution:
    def isPalindrome(self, s: str) -> bool:
        #first, i want to normalize it so that it is all lowercase
        s = s.lower()

        i = 0
        j = len(s) - 1

        while i < j:
            while i < j and not s[i].isalnum():
                i +=1
                #skip it if its not alphanumeric
            while i < j and not s[j].isalnum():
                j -= 1
                #skip it if its not alphanumeric
            
            if s[i] != s[j]:
                return False

            i += 1
            j -= 1
        
        return True