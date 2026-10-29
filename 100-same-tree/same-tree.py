# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        if p is None and q is None:
            return True

        if p is None or q is None:
            return False

        isSameLeft = self.isSameTree(p.left, q.left)
        isSameRight = self.isSameTree(p.right, q.right)

        return p.val == q.val and isSameLeft and isSameRight



