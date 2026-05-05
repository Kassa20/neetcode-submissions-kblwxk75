class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        _map = defaultdict(int)
        l = 0
        res = 0

        for r in range(len(s)):
            while _map[s[r]]:
                _map[s[l]] -= 1
                if _map[s[l]] == 0:
                    del _map[s[l]]
                l += 1
            
            _map[s[r]] += 1
            res = max(res, r - l + 1)
        
        return res

"""
m = 3

x: 1
y: 1

        l   r
z x y z x y z

"""



