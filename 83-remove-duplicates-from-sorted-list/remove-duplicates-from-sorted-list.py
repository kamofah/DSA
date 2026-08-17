# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        duplicate_set = set()
        current = head
        prev = ListNode(None, head)

        while current:
            if current.val not in duplicate_set:
                duplicate_set.add(current.val)
                prev = prev.next
            else:
                prev.next = current.next
            
            current = current.next
            
        return head
        