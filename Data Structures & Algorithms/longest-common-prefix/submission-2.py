class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        strs.sort()
        pre = strs[0]

        for i in range(1, len(strs)):
            curr = strs[i]
            same = ""
            for k in range(min(len(curr), len(pre))):
                if curr[k] != pre[k]:
                    break
                same += curr[k]
            
            pre = same
        
        return pre

