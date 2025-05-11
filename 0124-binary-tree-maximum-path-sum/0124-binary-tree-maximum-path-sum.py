# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max_path_val = float('-inf')

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def max_path(node):
            if not node:
                return 0

            left_max = max(max_path(node.left), 0)
            right_max = max(max_path(node.right), 0)

            current_max = left_max + right_max + node.val

            self.max_path_val = max(current_max, self.max_path_val)

            return node.val + max(left_max, right_max)


        max_path(root)

        return self.max_path_val
        