# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        nex = head.next
        prev = None

        while head != None:
            head.next = prev
            prev = head
            head = nex
            if head != None:
                nex = head.next

        return prev

        #            p  h  n
        # <-0<-1<-2<-3



