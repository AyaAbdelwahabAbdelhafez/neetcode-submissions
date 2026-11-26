class Solution:
    def isValid(self, s: str) -> bool:
        Valid_close={'(': ')', '{': '}', '[': ']'}
        stack=[]
        for p in s:
            if p in Valid_close.keys():
               stack.append(p)
            else:
                if not stack:
                    return False
                if Valid_close[stack[-1] ]==p:
                    stack.pop()
                else:
                    return False
        return len(stack) ==0
             
