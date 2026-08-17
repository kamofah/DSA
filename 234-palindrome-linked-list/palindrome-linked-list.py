# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        palindrome_list = []
        current = head

        while current:
            palindrome_list.append(current.val)
            current = current.next

        left = 0
        right = len(palindrome_list) - 1
        while left < right:
            if palindrome_list[left] != palindrome_list[right]:
                return False
            left += 1
            right -= 1

        return True