class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort()
        stack = []

        for p, s in pair[::-1]:
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()            

        return len(stack)

"""

d = 6
v = 2

d = vt
t = 6 / 2 = 3
----------------------
d = 9
v = 3
t = 9/3 = 3

"""