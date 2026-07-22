class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        trips.sort(key=lambda x: x[1]) 
        pos = [0] * 1000

        for trip in trips:
            p, src, dest = trip[0], trip[1], trip[2]

            for i in range(src+1, dest):
                pos[i] += p
            pos[src] += p
            pos[dest] -= p


        for p in pos:
            if p > capacity:
                return False


        return True



"""

1: +2
2: +2 + (+3) = +5
3: -2+3 = +1


"""