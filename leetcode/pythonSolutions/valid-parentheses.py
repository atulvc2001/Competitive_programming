class Solution:
    def isValid(self, s: str) -> bool:
        close = {")":"(","}":"{","]":"["}
        stack = []
        for i in s:
            if i in close:
                if stack and stack[-1] == close[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
            
        return True if not stack else False
