# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:

        def dfs(node, seen):
            nonlocal ans
            ## if value already in set, remove it
            ## because, all even frequency at the end of dfs will make palindrom
            ## also if there is one odd freq allowed to make it palindrom.
            if node.val in seen:
                seen.remove(node.val)
            else:
                seen.add(node.val)

            if node.left:
                dfs(node.left, seen.copy())
            
            if node.right:
                dfs(node.right, seen.copy())

            # if we are at leaf, check the set length for 1
            # 0 length means all the count(digit) are in even number
            # 1 length means all other counts are even, except one
            if not node.left and not node.right:
                if len(seen) <=1:
                    ans += 1

        ans = 0
        dfs(root, set())
        return ans
        
