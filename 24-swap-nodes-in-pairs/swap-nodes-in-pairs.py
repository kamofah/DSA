# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None: 
            return head 
        
        dummy = ListNode(None, None)

        final = dummy
        current = head
        while current and current.next:
            next_node = current.next
            current.next = current.next.next

            next_node.next = current
            dummy.next = next_node
            
            dummy = current
            current = current.next

        return final.next