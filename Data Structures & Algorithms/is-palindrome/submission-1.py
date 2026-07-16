class Solution:
    def isPalindrome(self, s: str) -> bool:
        #we have to remove punctuation from the input and also make it lowercase

        s = s.lower() #make it lowercase
        i = 0
        j = len(s) - 1

        while i < j:
            if not s[i].isalnum(): #if the character is not alphanumeric
                i += 1
                continue #the continue is necessary to actually move to the next iteration
            if not s[j].isalnum():
                j -= 1
                continue #we are skipping to the next iteration
            #now that we have verified that the characters pointed to by both pointers are alphanum, lets check that they are actually equal
            
            if s[i] != s[j]:
                return False
            #if they are equal 
            i+= 1
            j-= 1
        
        return True #if we've made it to this point without returning False
