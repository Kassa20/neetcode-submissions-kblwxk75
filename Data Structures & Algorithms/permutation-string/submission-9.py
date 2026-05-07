class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        s1Count = [0] * 26
        for c in s1:
            s1Count[ord(c) - ord('a')] += 1

        for i in range(len(s2)):
            s2Count = [0] * 26
            for j in range(i, len(s2)):
                index = ord(s2[j]) - ord('a')
                s2Count[index] += 1
                if s2Count[index] > s1Count[index]:
                    break
                if sum(s1Count) == sum(s2Count):
                    return True
        
        return False