class Solution:
    def checkIfExist(self, arr: List[int]):
        map_repeat = {}
        for i in range(len(arr)):
            if arr[i]*2 in map_repeat or arr[i]%2 == 0 and arr[i]//2 in map_repeat:
                return True
            map_repeat[arr[i]] = i
        return False
            
        
        
