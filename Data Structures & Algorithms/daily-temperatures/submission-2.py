class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
                
        res = []
        for i in range(len(t)):
            count = 1
            temp1 = t[i]
            found = False
            for j in range(i + 1, len(t)):
                temp2 = t[j]
                if temp2 > temp1:
                    found = True
                    res.append(count)
                    break
                count += 1
            if found == False:
                res.append(0)

        return res