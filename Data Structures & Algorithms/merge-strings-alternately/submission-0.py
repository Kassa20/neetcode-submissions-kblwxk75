class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        res = []
        p, p2 = 0, 0

        while p < len(word1) and p2 < len(word2):
            res.append(word1[p])
            res.append(word2[p2])
            p += 1
            p2 += 1

        while p < len(word1):
            res.append(word1[p])
            p += 1
        while p2 < len(word2):
            res.append(word2[p2])
            p2 += 1
        
        return ''.join(res)