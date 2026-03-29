class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        d = defaultdict(int)
        n = len(s)
        left = 0
        res = 0
        for right in range(n):
            c = s[right]
            d[c] += 1
            freq = 0
            for m in d:
                freq = max(freq, d[m])

            while (right - left + 1) - freq > k:
                c2 = s[left]
                d[c2] -= 1
                for m in d:
                    freq = max(freq, d[m])
                left += 1
            
            res = max(res, right - left + 1)

        return res
                
            
                

