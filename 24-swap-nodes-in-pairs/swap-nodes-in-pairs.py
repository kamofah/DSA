# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        current = head

        while current and current.next:
            second = current.next
            current.next = second.next
            second.next = current
            prev.next = second

            prev = current
            current = current.next

        return dummy.next