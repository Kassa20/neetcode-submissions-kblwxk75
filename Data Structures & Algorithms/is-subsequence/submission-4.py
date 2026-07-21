class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        index = 0
        matched = 0
        i = 0
        while i < len(s):
            while index < len(t) and s[i] != t[index]:
                index += 1

            if index >= len(t):
                return False

            matched += 1
            i += 1
            index += 1


        return matched == len(s)            

