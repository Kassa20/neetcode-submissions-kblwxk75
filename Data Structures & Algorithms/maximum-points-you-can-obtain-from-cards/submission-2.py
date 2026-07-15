class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        
        n = len(cardPoints)
        total = sum(cardPoints)
        window = n - k
        print("total: ", total)
        curr = sum(cardPoints[:window])
        minWindow = curr
        r = window

        while r < n:
            curr += cardPoints[r]
            curr -= cardPoints[r - window]
            minWindow = min(minWindow, curr)
            print("curr: ", curr)
            print("minWindow: ", minWindow)
            
            r += 1


        return total - minWindow
