# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def equalToDescendants(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            nonlocal res

            if not node:
                return 0
                
            left = dfs(node.left)
            right = dfs(node.right)
            if node.val == left + right:
                res += 1
            return node.val + left + right

        res = 0
        dfs(root)
        return res
