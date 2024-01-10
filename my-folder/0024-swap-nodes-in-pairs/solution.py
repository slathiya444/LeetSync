# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        ## base case
        if not head or not head.next:
            return head

        # define the nodes to bhe swapped
        first = head
        second = head.next

        # swapp nodes
        first.next = self.swapPairs(second.next)
        second.next = first

        # as gthe 2nd node will be new head, return new head(second)
        return second
        
