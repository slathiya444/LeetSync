# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        while q:
            ele = q.popleft()
            # we should go from right to left
            # if we go lft to right, we have to reiterate for left value in last level traversal
            # insert right if not null
            if right := ele.right: q.append(right)
            # insert left if not null
            if left := ele.left: q.append(left)

        return ele.val
        
