# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous_node = None
        pointer = head
        
        while pointer:
            next_node = pointer.next
            pointer.next = previous_node
            previous_node = pointer
            pointer = next_node
        return previous_node

        
