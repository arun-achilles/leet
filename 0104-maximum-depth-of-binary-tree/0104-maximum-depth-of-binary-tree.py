# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max_depth = 0

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def max_depth(node, depth):
            if node.left:
                max_depth(node.left, depth+1)
            if node.right:
                max_depth(node.right, depth+1)
            self.max_depth = max(self.max_depth, depth)

        if not root:
            return 0
        max_depth(root, 0)

        return self.max_depth + 1
        