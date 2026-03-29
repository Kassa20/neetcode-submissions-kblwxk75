class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        seen = set()
        res = []

        for i in range(len(strs)):
            c = strs[i]
            lis = []
            if c in seen:
                continue
            seen.add(c)
            lis.append(c)
            for j in range(i+1, len(strs)):
                t = strs[j]
                if t != c and t in seen:
                    continue
                if self.check(c, t):
                    lis.append(t)
                    seen.add(t)
            res.append(lis)
        
        return res

    def check(self, s, t):
        if len(s) != len(t):
            return False

        d1 = defaultdict(int)
        d2 = defaultdict(int)

        for i in range(len(s)):
            d1[s[i]] += 1
            d2[t[i]] += 1

        return d1 == d2





