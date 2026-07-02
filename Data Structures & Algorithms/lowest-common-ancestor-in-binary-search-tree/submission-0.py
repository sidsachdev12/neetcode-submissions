# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        def path_to_target(root, target):
            arr = [root]

            if root.val == target.val:
                return arr

            if target.val < root.val:
                arr += path_to_target(root.left, target)
            else:
                arr += path_to_target(root.right, target)

            return arr

        path_p = path_to_target(root, p)
        path_q = path_to_target(root, q)

        index_p, index_q = 0, 0

        while index_p < len(path_p) and index_q < len(path_q) and path_p[index_p].val == path_q[index_q].val:
            index_p += 1
            index_q += 1

        return path_p[index_p - 1]
        