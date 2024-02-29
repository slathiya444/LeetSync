# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        isEven = True
        q = deque([root])

        while q:
            prev = float('-inf') if isEven else float('inf')
            for _ in range(len(q)):
                
                node = q.popleft()
                # if even level:
                if isEven:
                    if node.val % 2 == 0 or node.val <= prev:
                        return False

                # if odd level
                else:
                    if node.val % 2 != 0 or node.val >= prev:
                        return False

                ## append the left child to que
                if node.left : q.append(node.left)
                ## append the right child to queue
                if node.right : q.append(node.right)

                prev = node.val

            isEven = not isEven

        return True
