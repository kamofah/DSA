# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = fast = head
        #  Get to the middle
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # Split linked List
        second = slow.next
        slow.next = None

        # Reverse second half
        prev = None
        while second:
            next_node = second.next
            second.next = prev
            prev = second
            second = next_node

        # merge first and second half of list
        first = head
        second = prev

        while second:
            next_first = first.next
            next_second = second.next

            first.next = second
            second.next = next_first

            first = next_first
            second = next_second

            