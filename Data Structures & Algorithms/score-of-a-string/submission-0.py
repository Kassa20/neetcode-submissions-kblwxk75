class Solution:
    def scoreOfString(self, s: str) -> int:
        
        res = 0
        for i in range(len(s) - 1):
            c = s[i]
            c2 = s[i + 1]
            res += abs(ord(c) - ord(c2))

        return res
