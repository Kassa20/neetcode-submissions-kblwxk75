class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        
        res = [0] * len(t)
        for i in range(len(t)-1):
            found = False
            days = 0
            temp = t[i]
            for j in range(i+1, len(t)):
                days += 1
                if t[j] > temp:
                    found = True
                    res[i] = days
                    break
            
            if found == False:
                res[i] = 0

        
        return res