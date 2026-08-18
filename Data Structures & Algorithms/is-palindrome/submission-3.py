class Solution:
    def isPalindrome(self, s: str) -> bool:
        #first we need to normalize the input by making it lowercase
        s = s.lower()

        #need two pointers
        #one pointer starts at the start of the string
        #the other pointer starts at the end of the string
        i = 0
        j = len(s) - 1

        while i < j: #loop runs while i and j don't cross each other
        #skipping spaces, punctuation, or symbols (non letters and numbers)
            while i < j and not s[i].isalnum(): 
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1
            
            if s[i] != s[j]:
                return False
            else: #go to the next character and compare
                i += 1
                j -= 1
        
        #if we are at this point and we have returned False yet, we can return true
        return True



