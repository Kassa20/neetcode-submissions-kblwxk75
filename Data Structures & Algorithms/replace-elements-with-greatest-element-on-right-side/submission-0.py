class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        n = len(arr)
        max_num = arr[n-1]
        res = [0] * n
        for i in range(n - 2, -1, -1):
            res[i] = max_num
            max_num = max(max_num, arr[i])

        res[n - 1] = -1

        return res

 