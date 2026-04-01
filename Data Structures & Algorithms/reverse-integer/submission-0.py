class Solution:
    def reverse(self, x: int) -> int:
        
        res = 0
        isN = False
        if x < 0:
            isN = True
            x = x * -1

        while x:
            z = x % 10
            res = res * 10 + z
            x = x // 10
        
        if isN:
            res *= -1
        
        if res < -2**31 or res > 2**31 - 1:
            return 0


        return res 


