# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        tmp = head
        arr = []
        while tmp:
            arr.append(tmp)
            tmp = tmp.next

        res = [0] * len(arr)
        left, right = 0, len(arr) - 1

        index = 0
        while index < len(arr): 
            res[index] = arr[left]
            index += 2
            left += 1

        index = 1
        while index < len(arr): 
            res[index] = arr[right]
            index += 2
            right -= 1

        for i in range(len(res) - 1):
            res[i].next = res[i+1]

        res[len(res)-1].next = None

"""

head = 2
    
    i
[2, 10, 4, 8, 6]

"""


