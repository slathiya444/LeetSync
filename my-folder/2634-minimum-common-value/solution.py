class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        long_list = nums1 if len(nums1) >= len(nums2) else nums2
        list_set = set(long_list)

        for i in (nums1 if len(nums1) < len(nums2) else nums2):
            if i in list_set:
                return i
        return -1

