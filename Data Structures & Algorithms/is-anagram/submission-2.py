class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        d1 = defaultdict(int)
        d2 = defaultdict(int)
        for c in s:
            d1[c] += 1
        for c in t:
            d2[c] += 1
        
        for c in s:
            if c not in t or d1[c] != d2[c]:
                return False

        return True        