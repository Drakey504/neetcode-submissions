class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        for c in s:      

            if len(stack) != 0 and c in ('}', ']', ')'):
                top = stack[-1]
                if (top == '{' and c == '}') or (top == '[' and c == ']') or (top == '(' and c == ')'):
                    stack.pop()
                else:
                    return False    
            else:    
                stack.append(c)   
                

        if len(stack) == 0:
            return True
        else:
            return False            
        