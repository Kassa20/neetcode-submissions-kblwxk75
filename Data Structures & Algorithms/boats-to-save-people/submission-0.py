class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        people.sort()
        left, right = 0, len(people) - 1
        res = 0

        while left < right:
            if people[left] + people[right] <= limit:
                res += 1
                left += 1
                right -= 1
            
            else:
                res += 1
                right -= 1                

        # print(left)
        # print(right)
        if left == right:
            res += 1


        return res


        # [1, 2, 4, 5]

        # [1, 2, 2, 3, 3]






