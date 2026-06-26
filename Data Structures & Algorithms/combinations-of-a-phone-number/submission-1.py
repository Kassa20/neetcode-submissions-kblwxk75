class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if len(digits) == 0:
            return []

        d = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }


        res = []
        def dfs(index, curr):
            if index > len(digits):
                return

            if len(curr) == len(digits):
                res.append(curr)
                return

            for c in d[digits[index]]:
                dfs(index + 1, curr + c)

            return

        dfs(0, "")


        return res





