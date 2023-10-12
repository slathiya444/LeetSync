# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def longest_path(node: TreeNode) -> int:
            if not node:
                return 0
            
            nonlocal diameter

            left_path = longest_path(node.left)
            right_path = longest_path(node.right)

            length = left_path + right_path
            diameter = max(diameter, length)

            return max(left_path, right_path)+1
        longest_path(root)
        return diameter

