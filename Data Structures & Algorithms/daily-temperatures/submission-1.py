class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
                
        res = [0] * len(t)
        stack = []

        for i, t in enumerate(t):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append((t, i))
        return res