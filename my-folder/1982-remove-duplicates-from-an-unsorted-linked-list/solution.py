# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        def scan(head):
            while head:
                yield head.val
                head = head.next
        cnt = Counter(scan(head))
        pre = ListNode()
        curr = pre
        for val in scan(head):
            if cnt[val] == 1:
                curr.next = ListNode(val)
                curr = curr.next
        return pre.next
