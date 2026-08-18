class Solution:
    def isPalindrome(self, s: str) -> bool:
        #in this other solution, we can preprocess the string first to remove non alphanumeric characters

        #first lets normalize the string
        s = s.lower()

        #then remove characters that arent alphanumeric
        s = "".join(char for char in s if char.isalnum())
        #note, we can do the alphanumeric character removal and string normalizing in one step

        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            else:
                i += 1
                j -= 1
        
        return True