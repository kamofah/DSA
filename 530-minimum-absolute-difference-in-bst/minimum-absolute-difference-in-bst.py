# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        stack = [root]
        visited = []

        while stack:
            current = stack.pop()
            visited.append(current.val)

            if current.right:
                stack.append(current.right)
            
            if current.left:
                stack.append(current.left)


        absDif = float('inf')
        for i in range(len(visited)):
            for j in range(i + 1, len(visited)):
                absDif = min(absDif, abs(visited[i] - visited[j]))

        return absDif