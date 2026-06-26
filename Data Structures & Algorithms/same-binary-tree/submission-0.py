# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        left = True
        right = True
        if p and q:
            if p.val == q.val:
                left = left and self.isSameTree(p.left, q.left)
                right = right and self.isSameTree(p.right, q.right)
            else:
                return False
        elif p is None and q is None:
            return True
        else:
            return False

        if left and right:
            return True
        else:
            return False
