class Solution:
    def isValid(self, s: str) -> bool:
        
        if len(s) % 2 != 0:
            return False
        
        stack = []
        for char in s:
            #if its an opening delimeter
            if char in '({[':
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                elif (char == ')' and stack.pop() != '(') or (char == '}' and stack.pop() != '{') or (char == ']' and stack.pop() != '['):
                    return False
        
        return len(stack) == 0

                
                
