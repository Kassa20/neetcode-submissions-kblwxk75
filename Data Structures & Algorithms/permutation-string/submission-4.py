class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        left, right = 0, len(s1) - 1
        dict1 = defaultdict(int)

        for c in s1:
            dict1[c] += 1

        while right < len(s2):
            dict2 = defaultdict(int)
            window = s2[left:right + 1]
            count = 0
            for c in window:
                dict2[c] += 1
   
            for key, value in dict2.items():
                if key not in dict1.keys():
                    break
                if dict2[key] != dict1[key]:
                    break
                if dict1 == dict2:
                    return True
            left += 1
            right += 1
        return False