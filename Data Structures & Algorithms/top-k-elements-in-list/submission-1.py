class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:


        d = defaultdict(int)
        res = []
        for num in nums:
            d[num] += 1

        # [1, 2] k = 2
        sorted_d = dict(sorted(d.items(), key=lambda item:item[1]))
        temp = list(sorted_d.keys())

        index = len(temp)-1
        for i in range(k):
            res.append(temp[index])
            index -= 1

        return res

        
        