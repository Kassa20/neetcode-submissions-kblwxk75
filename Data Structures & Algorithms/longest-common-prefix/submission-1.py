class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if len(strs) <= 1:
            return strs[0]

        strs = sorted(strs)
        window = strs[0]

        for i in range(1, len(strs)):
            same = ""
            for j in range(len(window)):
                if window[j] != strs[i][j]:
                    break
                same += window[j]
            window = same


        return window