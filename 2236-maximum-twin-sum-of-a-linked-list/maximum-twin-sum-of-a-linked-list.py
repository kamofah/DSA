# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        maximum_sum = 0
        slow = fast = head

        # Find start of second half
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse second half
        current = slow
        prev = None

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        # Compare twin nodes
        start = head
        second = prev

        while second:
            maximum_sum = max(maximum_sum, start.val + second.val)
            start = start.next
            second = second.next

        return maximum_sum
        