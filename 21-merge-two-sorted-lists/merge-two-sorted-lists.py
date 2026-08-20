# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(None, None)
        l1_pointer = l1
        l2_pointer = l2

        current = dummy
        while l1_pointer and l2_pointer:
            if l1_pointer.val <= l2_pointer.val:
                current.next = l1_pointer
                l1_pointer = l1_pointer.next
            else:
                current.next = l2_pointer
                l2_pointer = l2_pointer.next
            
            current = current.next

        if l1_pointer:
            current.next = l1_pointer
        else:
            current.next = l2_pointer

        return dummy.next
        