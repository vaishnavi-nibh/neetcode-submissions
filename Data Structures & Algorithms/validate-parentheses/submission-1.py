class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            else: 
                #this means you have some closing delimeter with no corresponding opening delimeter
                if len(stack) == 0:
                    return False
                if char == ']':
                    if stack.pop() != '[':
                        return False
                if char == ')':
                    if stack.pop() != '(':
                        return False
                if char == '}':
                    if stack.pop() != '{':
                        return False
        
        return len(stack) == 0 #the stack should be empty 
