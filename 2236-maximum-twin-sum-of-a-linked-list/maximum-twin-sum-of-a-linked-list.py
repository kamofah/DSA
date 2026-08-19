# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        maximum_sum = 0
        slow = fast = head

        #  Get to the middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the middle
        current = slow
        prev = None
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        # Calculate maximum_sum with prev and slow
        slow = head
        while prev:
            maximum_sum = max(maximum_sum, slow.val + prev.val)
            slow = slow.next
            prev = prev.next

        return maximum_sum

        