# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def frequenciesOfElements(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ## traverse the linkedlist for mapp
        node = head
        mapp = {}
        while node:
            mapp[node.val] = mapp.get(node.val, 0) + 1
            node = node.next

        new_head = temp = ListNode()
        for val in mapp.values():
            temp.next = ListNode(val)
            temp = temp.next
        return new_head.next
        
