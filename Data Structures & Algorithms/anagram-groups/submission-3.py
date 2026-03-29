class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = []
        seen = set()

        for r in range(len(strs)): # O(n^2)
            s = strs[r]
            if s in seen:
                continue
            anagram = []
            freq = defaultdict(int)
            anagram.append(s)
            seen.add(s)
            for c in s:
                freq[c] += 1

            for window in range(r+1, len(strs)):
                freq2 = defaultdict(int)
                s2 = strs[window]
                for c in s2:
                    freq2[c] += 1
                if freq == freq2:
                    seen.add(s2)
                    anagram.append(s2)

            res.append(anagram)


        return res




