# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        count = 0

        while current is not None:
            count += 1
            current = current.next
        
        current = head
        mid = count // 2
        while mid is not 0: 
            current = current.next
            mid -= 1

        return current