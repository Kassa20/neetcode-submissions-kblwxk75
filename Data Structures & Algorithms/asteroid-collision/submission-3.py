class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        stack = []
        for a in asteroids:
            if not stack:
                stack.append(a)
                continue

            while stack and stack[-1] > 0 and a < 0:
                diff = stack[-1] - abs(a)
                if diff < 0:
                    stack.pop()
                elif diff > 0:
                    a = 0
                elif diff == 0:
                    a = 0
                    stack.pop()
            
            if a != 0:
                stack.append(a)

        return stack


