# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.lowest = None

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def inorder(curr, p, q):
            print(curr.val)
            if not curr:
                return
            self.lowest = curr
            if curr.val > p.val and curr.val > q.val:
                inorder(curr.left, p, q)
            elif curr.val < p.val and curr.val < q.val:
                inorder(curr.right, p, q)
        inorder(root, p, q)
        return self.lowest    