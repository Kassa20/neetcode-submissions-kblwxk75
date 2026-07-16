class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        d = defaultdict(int)
        
        for cap, src, dest in trips:
            d[src] += cap
            d[dest] -= cap
        

        curr = 0
        for loc in sorted(d.keys()):
            curr += d[loc]
            if curr > capacity:
                return False


        return True
