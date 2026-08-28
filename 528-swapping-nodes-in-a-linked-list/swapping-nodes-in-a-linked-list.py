# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        size = 0
        current = head

        while current:
            current = current.next
            size += 1

        first = head
        for _ in range(k - 1):
            first = first.next

        second = head
        for _ in range(size - k):
            second = second.next

        first.val, second.val = second.val, first.val

        return head