class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        if len(hand) % groupSize != 0:
            return False

        d = defaultdict(int)
        for n in hand:
            d[n] += 1

        minH = list(d.keys())     
        heapq.heapify(minH)

        while minH:
            first = minH[0]
            for i in range(first, first + groupSize):
                if i not in d:   
                    return False
                d[i] -= 1
                if d[i] == 0:
                    if i != minH[0]:
                        return False
                    heapq.heappop(minH)

        return True

"""

[1, 2, 2, 3, 3, 4, 6, 7, 8]

[1, 2, 2, 3, 3, 4, 4, 5]



"""



