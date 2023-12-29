# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None

        while len(lists)> 1:
            mergedList = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1 < len(lists) else None

                mergedList.append(self.mergeList(l1, l2))

            lists = mergedList

        return lists[0]

    def mergeList(self, l1, l2):
        if l1 is None:
            return l2

        if l2 is None:
            return l1

        if l1.val < l2.val:
            l1.next = self.mergeList(l1.next, l2)
            return l1

        else:
            l2.next = self.mergeList(l1, l2.next)
            return l2
        
