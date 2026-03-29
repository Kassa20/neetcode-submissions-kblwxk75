class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
                
        res = [0]*len(t)
        stack = []

        for i, temp in enumerate(t):
            while stack and stack[-1][1] < temp:
                index, stackT = stack.pop()
                res[index] = i - index
            stack.append([i, temp])

        return res






