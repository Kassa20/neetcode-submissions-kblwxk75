class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        stack = []
        commands = ["+", "D", "C"]

        for op in operations:
            if op not in commands:
                num = int(op)
            if op == "+":
                num = stack[-1] + stack[-2]
            if op == "D":
                num = 2 * stack[-1]
            if op == "C":
                stack.pop()
                continue
            stack.append(num)
        
        res = sum(stack)

        return res
                
        

