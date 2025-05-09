# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Memo:
    def __init__(self, k):
        self.k = k
        self.result = None

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        def traverse(curr, memo):
            if not curr or memo.result is not None:
                return
            traverse(curr.left, memo)
            memo.k -= 1
            if memo.k == 0:
                memo.result =  curr.val
            traverse(curr.right, memo)
        
        memo = Memo(k)
        traverse(root, memo)
        return memo.result

