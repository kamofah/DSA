# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:
        if root is None:
            return False

        if self.dfs(root) == self.dfs(subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def dfs(self, root):
        stack = [root]
        visited = []

        while stack:
            current = stack.pop()

            if current is None:
                visited.append(None)
                continue

            visited.append(current.val)

            stack.append(current.right)
            stack.append(current.left)

        return visited