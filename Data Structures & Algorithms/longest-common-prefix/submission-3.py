class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        strs.sort()

        for k in range(min(len(strs[0]), len(strs[-1]))):
            if strs[0][k] != strs[-1][k]:
                return strs[0][:k]
                
        return strs[0]

