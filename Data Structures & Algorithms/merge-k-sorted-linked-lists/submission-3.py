# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if not lists:
            return None

        interval = lists[0]
        for i in range(1, len(lists)):
            lis = lists[i]
            if interval.val < lis.val:
                order = ListNode(interval.val)
            else:
                order = ListNode(lis.val)
            head = order

            while interval and lis:
                if interval.val < lis.val:
                    head.next = ListNode(interval.val)
                    interval = interval.next
                else:
                    head.next = ListNode(lis.val)
                    lis = lis.next
                head = head.next

            if interval:
                head.next = interval
            if lis:
                head.next = lis

            interval = order.next


        return interval

