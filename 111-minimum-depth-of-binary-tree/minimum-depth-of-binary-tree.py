# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode | None) -> int:
        if root is None:
            return 0

        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        
        if left == 0 or right == 0:
            return 1 + max(left, right)
        
        return 1 + min(left, right)