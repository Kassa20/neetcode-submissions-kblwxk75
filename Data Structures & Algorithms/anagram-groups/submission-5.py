class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        d = defaultdict(list)
        for s in strs: 
            count = [0]*26
            for c in s:
                index = ord(c) - ord('a')
                count[index] += 1

            d[tuple(count)].append(s)
        
        res = []
        for v in d:
            res.append(d[v])


        return res