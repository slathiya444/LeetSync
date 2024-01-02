# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []
        arr = self.helper(root, arr)
        return arr[k-1]

    def helper(self, root, arr):
        if not root:
            return arr 

        self.helper(root.left, arr)
        arr.append(root.val)
        self.helper(root.right, arr)   

        return arr
        
