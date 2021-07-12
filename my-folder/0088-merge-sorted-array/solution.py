class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(len(nums1),m,-1):
            nums1.pop(m)
        for i in nums2[:n]:
            nums1.append(i)
        nums1.sort()
