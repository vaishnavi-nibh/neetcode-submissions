class Solution:
    def isValid(self, s: str) -> bool:
        #reimplementing valid paranthesis using dictionary
        pairs = {
            ']': '[',
            '}': '{',
            ')': '('
        }

        if len(s) % 2 != 0:
            return False
        
        stack = []

        for char in s:
            if char in '{([':
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                elif stack.pop() != pairs[char]:
                    return False
        
        return len(stack) == 0