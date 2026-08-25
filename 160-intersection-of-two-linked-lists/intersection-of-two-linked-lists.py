# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from collections import Counter
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        node_counter = Counter()
        
        while headA:
            node_counter[headA] += 1
            headA = headA.next

        while headB:
            node_counter[headB] += 1
            if node_counter[headB] > 1:
                return headB
            headB = headB.next

        return None