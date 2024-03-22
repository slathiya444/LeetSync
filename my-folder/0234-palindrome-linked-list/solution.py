# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        curr = head
        dummy_val = []
        while curr:
            dummy_val.append(curr.val)
            curr = curr.next

        return dummy_val == dummy_val[::-1]

        
        
