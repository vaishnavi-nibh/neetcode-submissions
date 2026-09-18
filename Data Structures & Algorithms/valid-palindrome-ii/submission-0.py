class Solution:
    def validPalindrome(self, s: str) -> bool:
        #we have one chance of deleting something, when we get to a mismatch we have to see, deleting which letter leads us to a palindrome
        #so for example if we have abbca 
        #and we compare b and c, and clearly they are mismatch
        #now we have to decide: do we remove b or do we remove c

        #so to check this, we have already validated that the things before b and c are valid for palindromes, therefore lets check, lets say we remove the left letter (b) --> is i + 1 to j a valid palindrome --> if so, remove b!
        #now, lets say we remove the right letter (c) --> is i to j - 1 (where j points to c) a valid palindrome --> if yes, remove c!

        #if neither of the subwindows form valid palindromes, then that means we'd have to remove more than 1 character for it to be a valid palindrome, so return False
        i = 0
        j = len(s) - 1

        while i < j:
            if s[i] != s[j]:
                leftPal = True
                rightPal = True
                #check if i+1 to j is a valid palindrome, in which case we delete left
                k = i + 1
                l = j
                while k < l:
                    if s[k] != s[l]:
                        leftPal = False
                        break
                    k += 1
                    l -= 1
            
                #check if i to j - 1 is the valid palindrome (in which case we delete right)
                k = i
                l = j - 1
                while k < l:
                    if s[k] != s[l]:
                        rightPal = False
                        break
                    k += 1
                    l -= 1
            
                #if one of the subwindows is a palindrome
                if leftPal or rightPal:
                    return True
                else: #if none of them are True, then despite deleting one of them we still cant get a valid palindrome
                    return False
            
            i += 1
            j -= 1

        return True    



