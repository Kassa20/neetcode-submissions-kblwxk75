class Solution:
    def customSortString(self, order: str, s: str) -> str:
        
        count = [0] * 26
        res = []

        for c in s:
            count[ord(c) - ord('a')] += 1
        
        for c in order:
            index = ord(c) - ord('a')
            
            while count[index]:
                res.append(c)
                count[index] -= 1
        

        for i in range(26):
            c = chr(ord('a') + i)

            while count[i]:
                count[i] -= 1
                res.append(c)


        return ''.join(res)


