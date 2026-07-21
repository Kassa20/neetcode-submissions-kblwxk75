class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0

        if len(s) == 0:
            return True

        for j in t:
            if i< len(s) and j == s[i]:
                i+=1

        return len(s) == i