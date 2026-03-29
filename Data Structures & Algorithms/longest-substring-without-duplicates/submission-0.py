class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        seen = set()
        left = 0
        res = 0

        for right in range(len(s)):
            c = s[right]
            while c in seen:
                seen.remove(s[left])
                left += 1

            seen.add(c)
            res = max(res, right-left+1)

        return res