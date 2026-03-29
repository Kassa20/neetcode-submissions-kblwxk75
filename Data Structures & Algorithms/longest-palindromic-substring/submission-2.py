class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        n = len(s)
        res = ""

        def ispalindrome(left, right):
            if left < 0 or right >= n:
                return False

            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            
            return True


        for i in range(n):
            test = s[i]
            left, right = i, i
            while ispalindrome(left, right):
                if right - left + 1 > len(res):
                    res = s[left:right+1]
                right += 1
                left -= 1
                
            test = s[i]
            left, right = i, i + 1
            while ispalindrome(left, right):
                if right - left + 1 > len(res):
                    res = s[left:right+1]
                right += 1
                left -= 1

        return res if res else test



#  l   r
#  a b c
