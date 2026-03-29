class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        stack = []
        commands = ["+", "D", "C"]

        for op in operations:
            if op not in commands:
                stack.append(int(op))
            if op == "+" and len(stack) >= 2:
                num = stack[-1] + stack[-2]
                stack.append(num)
            if op == "D" and stack:
                num = 2 * stack[-1]
                stack.append(num)
            if op == "C" and stack:
                stack.pop()
        
        res = sum(stack)

        return res
                
        

