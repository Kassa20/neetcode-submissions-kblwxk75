class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
    
        res = []

        for i in range(numRows):

            row = [1]

            if res:
                prev = res[-1]
                for j in range(len(prev) - 1):
                    row.append(prev[j] + prev[j+1])
            
                row.append(1)
            res.append(row)


        return res
