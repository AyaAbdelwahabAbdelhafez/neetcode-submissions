class Solution:
    def simplifyPath(self, path: str) -> str:
        parts = path.split('/')
        parts = list(filter(None, parts)) 
        stack=[]
        for part in parts:
            if part == ".":
                continue
            elif part =="..":
              if stack:
                stack.pop()
            else:
                stack.append(part)
        return "/"+"/".join(stack)
