# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = [[root]]
        result = [[root.val]]
        for level in queue:
            next_level = []
            for el in level:
                if el.left:
                    next_level.append(el.left)
                if el.right:
                    next_level.append(el.right)
            if next_level:
                queue.append(next_level)
                result.append([el.val for el in next_level])
        return result