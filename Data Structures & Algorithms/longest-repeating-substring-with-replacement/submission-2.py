class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0

        d = defaultdict(int)
        _max, l = 0, 0
        for r in range(len(s)):
            d[s[r]] += 1
            _max = max(_max, d[s[r]])

            while (r - l + 1) - _max > k:
                d[s[l]] -= 1
                if d[s[l]] == 0:
                    del d[s[l]]
                l += 1

            res = max(res, r - l + 1)
        

        return res
