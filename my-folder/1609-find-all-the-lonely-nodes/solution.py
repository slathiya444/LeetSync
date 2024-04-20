# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def dfs(node):
            ## if only left node is present:
            if node.left and not node.right:
                ans.append(node.left.val)
            
            ## if only right node is present:
            if node.right and not node.left:
                ans.append(node.right.val)

            if node.left:
                dfs(node.left)

            if node.right:
                dfs(node.right)

        dfs(root)
        return ans


        
