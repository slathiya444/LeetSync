class Solution:
    def duplicateZeros(self, arr: List[int]) -> List[int]:
        """
        Do not return anything, modify arr in-place instead.
        """
        i=0
        while i<len(arr):

            if arr[i] ==0:
                arr.pop()
                arr.insert(i+1,0)
                i=i+2
            else:
                i=i+1


                
