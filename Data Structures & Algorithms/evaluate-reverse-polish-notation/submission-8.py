class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        operators = ["+", "-", "*", "/"]
        for i in range(len(tokens)):

            curr = tokens[i]
            if stack and tokens[i] in operators:
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                if tokens[i] == "+":
                    curr = num1 + num2
                elif tokens[i] == "-":
                    curr = num1 - num2
                elif tokens[i] == "*":
                    curr = num1 * num2
                elif tokens[i] == "/":
                    curr = int(num1 / num2)
      
        
            stack.append(int(curr))


        return stack[-1]




"""

[1, 2] +
2 + 1 = 3
--------
[3, 3] *
3 * 3 = 9
--------
[9, 4] - 
9 - 4 = 5
--------
[5]

"""