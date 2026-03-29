class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        s = s.rstrip()
        s = s.lstrip()

        if not s:
            return 0
            
        i = len(s) - 1
        count = 0
        while i >= 0 and s[i] != " ":
            count += 1
            i -= 1
            

        return count