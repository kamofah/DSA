# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from collections import Counter
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        node_counter = Counter()
        current = head
        while current is not None:
            node_counter[current] += 1
            if node_counter[current] > 1:
                return True   
            current = current.next
        return False
            
