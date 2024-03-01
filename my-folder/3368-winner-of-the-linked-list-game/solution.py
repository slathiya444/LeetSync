# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def gameResult(self, head: Optional[ListNode]) -> str:
        even_team, odd_team = 0, 0
        even_p, odd_p = head, head.next
        while even_p and odd_p:
            if even_p.val > odd_p.val:
                even_team += 1
            else:
                odd_team += 1

            if odd_p.next:
                even_p = odd_p.next
                odd_p = even_p.next
            else: even_p, odd_p = None, None

        return "Even" if even_team > odd_team else ("Odd" if odd_team > even_team else "Tie")

        
