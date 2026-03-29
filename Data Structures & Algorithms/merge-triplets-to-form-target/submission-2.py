class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        n = len(triplets)
        interval = [0, 0, 0]
        for triplet in triplets:
            if triplet[0] <= target[0] and triplet[1] <= target[1] and triplet[2] <= target[2]:
                for k in range(3):
                    interval[k] = max(interval[k], triplet[k])
            
            if interval == target:
                return True

        return False



    