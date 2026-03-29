# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        minHeap = []

        for i, node in enumerate(lists):
            if node:
                heapq.heappush(minHeap, (node.val, i, node))
        
        head = ListNode()
        cur = head

        while minHeap:
            val, i, node = heapq.heappop(minHeap)
            cur.next = node
            cur = cur.next
            node = node.next
            if node:
                heapq.heappush(minHeap, (node.val, i, node))
        
        return head.next



