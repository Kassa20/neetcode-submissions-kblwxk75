class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0

        for i in range(len(s)):
            d = defaultdict(int)
            _max = 0
            for j in range(i, len(s)):
                d[s[j]] += 1
                _max = max(_max, d[s[j]])

                if (j - i + 1) - _max <= k:
                    res = max(res, j - i + 1)
        

        return res
