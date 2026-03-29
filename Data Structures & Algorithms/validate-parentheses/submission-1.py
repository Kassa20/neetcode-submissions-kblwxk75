class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        op = ["(", "{", "["]
        cl = [")", "]", "}"]
        
        for c in s:
            if c in op:
                stack.append(c)
            
            if c in cl:
                if not stack:
                    return False
                ma = stack.pop()
                if ((c == ")" and ma != "(") or
                    (c == "}" and ma != "{"  or
                    (c == "]" and ma != "["))):
                    return False
        
        return len(stack) == 0



