# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(node, max_value, min_value):
            ## base cases
            if not node:
                return

            nonlocal best

            best = max(best, max_value - node.val)
            best = max(best, node.val - min_value)

            max_value = max(node.val, max_value)
            min_value = min(node.val, min_value)

            dfs(node.left, max_value, min_value)
            dfs(node.right, max_value, min_value)

        inf = 10 ** 20
        best = 0
        dfs(root, -inf, inf)
        return best
