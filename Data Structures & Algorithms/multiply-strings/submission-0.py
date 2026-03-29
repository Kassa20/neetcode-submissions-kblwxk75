class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        res = 0
        res2 = 0
        n = len(num1)
        n2 = len(num2)
        ans = ""

        for i in range(n):
            z = ord(num1[i]) - ord('0')
            res = res * 10 + z
        for i in range(n2):
            z = ord(num2[i]) - ord('0')
            res2 = res2 * 10 + z

        f = res * res2
        f = str(f)

        return f