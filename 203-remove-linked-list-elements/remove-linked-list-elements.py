# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy_head = dummy
        current = head

        while current:
            if current.val != val:
                dummy.next = current
                dummy = dummy.next
            current = current.next
        
        dummy.next = None
        return dummy_head.next



        